Summary:	Powertweak - Tune system to optimal performance
Summary(pl):	Narzêdzie do optymalizacji wydajno¶ci systemu
Name:		powertweak
Version:	0.99.0
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
URL:		http://powertweak.sourceforge.net/
Vendor:		Dave Jones <dave@powertweak.com>
Source0:	http://download.sourceforge.net/powertweak/%{name}-%{version}.tar.bz2
ExclusiveArch:	%{ix86}
BuildRequires:	libxml-devel >= 1.8.8
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	ncurses-devel
BuildRequires:	gpm-devel
BuildRequires:	pciutils
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Powertweak is a utility for tweaking your Linux system to peak
performance. It can tune many parts of your system. Tunes PCI devices
to use optimal settings. Enables performance enhancing features of the
CPU(s).

%description -l pl
Powertweak to narzêdzie do optymalizacji Twojego systemu Linux. Mo¿e
on dostrajaæ wiele czê¶ci systemu jak np. urz±dzenia PCI, CPU itd.

%prep
%setup -q

%build
CPPFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -I/usr/include/ncurses"
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -I/usr/include/ncurses"
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses"
export CFLAGS CXXFLAGS CPPFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_datadir}}
install -d $RPM_BUILD_ROOT/var/log/powertweak

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* \
	ChangeLog README Release-notes Documentation/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,Release-notes,Documentation/*}.gz
%attr(755,root,root) %{_sbindir}/powertweak
%attr(755,root,root) %{_sbindir}/powertweak-config
%{_mandir}/man8/powertweak.8.gz
%{_datadir}/powertweak
/var/log/powertweak
