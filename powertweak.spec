Summary:	Powertweak - Tune system to optimal performance
Summary(pl):	Narzêdzie do optymalizacji wydajno¶ci systemu
Name:		powertweak
Version:	0.99.4
Release:	1
License:	GPL
Group:		Applications/System
Vendor:		Dave Jones <dave@powertweak.com>
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/powertweak/%{name}-%{version}.tar.bz2
Patch0:		%{name}-opt.patch
Patch1:		%{name}-acam.patch
Patch2:		%{name}-fix.patch
Patch3:		%{name}-morecpu.patch
URL:		http://powertweak.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.1.0
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xprefix	/usr/X11R6
%define		_xbindir	%{_xprefix}/bin
%define		_xmandir	%{_xprefix}/man

%description
Powertweak is a utility for tweaking your Linux system to peak
performance. It can tune many parts of your system. Tunes PCI devices
to use optimal settings. Enables performance enhancing features of the
CPU(s).

%description -l pl
Powertweak to narzêdzie do optymalizacji Twojego systemu Linux. Mo¿e
on dostrajaæ wiele czê¶ci systemu jak np. urz±dzenia PCI, CPU itd.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
CPPFLAGS="-I/usr/include/libxml2/libxml"
# ncurses must be here, not in CPPFLAGS
# (menu.h conflict - tvision/include dir must be before ncurses)
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -I/usr/include/ncurses"
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_xbindir},%{_mandir}/man8,%{_xmandir}/man8}
install -d $RPM_BUILD_ROOT/var/log/powertweak

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT{%{_bindir},%{_xbindir}}/gpowertweak
install distro/debian/powertweak-gtk.8x $RPM_BUILD_ROOT%{_xmandir}/man8/gpowertweak.8x
install distro/debian/powertweak-text.8 $RPM_BUILD_ROOT%{_mandir}/man8/powertweak.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO Documentation/*
%attr(755,root,root) %{_sbindir}/powertweakd
%dir /etc/powertweak
%config(noreplace) %verify(not size mtime md5) /etc/powertweak/tweaks
/var/log/powertweak
%{_datadir}/powertweak
%dir %{_libdir}/powertweak
%dir %{_libdir}/powertweak/plugins
%attr(755,root,root) %{_libdir}/powertweak/plugins/*.so*
# text
%attr(755,root,root) %{_bindir}/powertweak
%{_mandir}/man8/powertweak.8*
# GTK
%attr(755,root,root) %{_xbindir}/gpowertweak
%{_xmandir}/man8/gpowertweak.8x*
