Summary:	Powertweak - Tune system to optimal performance
Name:		powertweak
Version:	0.1.6
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
URL:		http://linux.powertweak.com
Vendor:		Dave Jones <dave@powertweak.com>
Source0:	%{name}-%{version}.tar.bz2
Patch0:		powertweak-DESTDIR.patch
Patch1:		powertweak-glibc.patch
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Powertweak is a utility for tweaking your Linux system to peak
performance. It can tune many parts of your system. Tunes PCI devices
to use optimal settings. Enables performance enhancing features of the
CPU(s).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cd lib
%configure %{version}
cd ..

make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_datadir}}
install -d $RPM_BUILD_ROOT/var/log/powertweak

make DESTDIR=$RPM_BUILD_ROOT install

strip --strip-unneeded $RPM_BUILD_ROOT%{_sbindir}/*

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
