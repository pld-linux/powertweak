Summary:	Powertweak - Tune system to optimal performance
Summary(pl.UTF-8):	Narzędzie do optymalizacji wydajności systemu
Name:		powertweak
Version:	0.99.5
Release:	1
License:	GPL v2
Group:		Applications/System
Vendor:		Dave Jones <dave@powertweak.com>
Source0:	http://dl.sourceforge.net/powertweak/%{name}-%{version}.tar.bz2
# Source0-md5:	fe7e147ae7536846411c6239e33e6959
Patch0:		%{name}-opt.patch
Patch1:		%{name}-acam.patch
Patch2:		%{name}-fix.patch
Patch3:		%{name}-morecpu.patch
Patch4:		%{name}-linux26.patch
Patch5:		%{name}-ioctl.patch
URL:		http://powertweak.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	gpm-devel
BuildRequires:	gtk+-devel >= 1.2.0
#BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.1.0
#BuildRequires:	ncurses-devel
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Powertweak is a utility for tweaking your Linux system to peak
performance. It can tune many parts of your system. Tunes PCI devices
to use optimal settings. Enables performance enhancing features of the
CPU(s).

%description -l pl.UTF-8
Powertweak to narzędzie do optymalizacji Twojego systemu Linux. Może
on dostrajać wiele części systemu jak np. urządzenia PCI, CPU itd.

%package gtk
Summary:	GTK+ GUI for Powertweak
Summary(pl.UTF-8):	Oparty na GTK+ interfejs do Powertweak
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gtk
GTK+-based GUI for Powertweak.

%description gtk -l pl.UTF-8
Oparty na GTK+ graficzny interfejs do narzędzia Powertweak.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
# disabled - tvision client is disabled in 0.99.5
## ncurses must be here, not in CPPFLAGS
## (menu.h conflict - tvision/include dir must be before ncurses)
#CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -I/usr/include/ncurses"
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man8

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/daemon/powertweakd.8 $RPM_BUILD_ROOT%{_mandir}/man8
install distro/debian/powertweak-gtk.8x $RPM_BUILD_ROOT%{_mandir}/man8/gpowertweak.8x
#install distro/debian/powertweak-text.8 $RPM_BUILD_ROOT%{_mandir}/man8/powertweak.8

rm -f $RPM_BUILD_ROOT%{_libdir}/powertweak/plugins{,/core}/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO Documentation/*
%attr(755,root,root) %{_sbindir}/powertweakd
%attr(755,root,root) %{_bindir}/lspowertweak
%dir %{_sysconfdir}/powertweak
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/powertweak/tweaks
%{_datadir}/powertweak
%dir %{_libdir}/powertweak
%dir %{_libdir}/powertweak/plugins
%attr(755,root,root) %{_libdir}/powertweak/plugins/*.so*
%dir %{_libdir}/powertweak/plugins/core
%attr(755,root,root) %{_libdir}/powertweak/plugins/core/*.so*
%{_mandir}/man8/powertweakd.8*

# text (disabled in 0.99.5)
#%attr(755,root,root) %{_bindir}/powertweak
#%{_mandir}/man8/powertweak.8*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpowertweak
%{_mandir}/man8/gpowertweak.8x*
