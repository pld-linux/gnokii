Summary:	Linux/Unix tool suite for mobile phones
Summary(pl):	Linuksowy/uniksowy zestaw narz�dzi dla telefon�w kom�rkowych
Name:		gnokii
Version:	0.6.4
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Communications
#Source0:	http://savannah.nongnu.org/download/gnokii/%{name}-%{version}.tar.bz2
Source0:	ftp://ftp.gnokii.org/pub/gnokii/%{name}-%{version}.tar.bz2
# Source0-md5:	e48e72b4038481509f32e2a7596dc2d5
# Source0-size:	2006834
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-pld.patch
Patch1:		%{name}-savesms-date.patch
URL:		http://www.gnokii.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel >= 2.8-2
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	libtool
Requires:	libgnokii = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnokii is a Linux/Unix tool suite and (eventually) modem/fax driver
for mobile phones.

%description -l pl
Gnokii jest zestawem narz�dzi dla Linuksa/Uniksa, oraz sterownikiem
modemu/faxu dla telefon�w kom�rkowych.

%package X11
Summary:	Graphical Linux/Unix tool suite for mobile phones
Summary(pl):	Zestaw narz�dzi z graficznym interfejsem dla telefon�w kom�rkowych
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description X11
Xgnokii is graphical Linux/Unix tool suite for mobile phones. It
allows you to edit your contacts book, send/read SMS's from/in
computer and more other features.

%description X11 -l pl
Xgnokii jest zestawem narz�dzi z graficznym interfejsem u�ytkownika do
pracy z telefonami kom�rkowymi. Pozwalaj� one na edytowanie spisu
telefon�w, wysy�anie/czytanie wiadomo�ci SMS i wiele innych rzeczy.

%package -n libgnokii
Summary:	A gnokii shared library
Summary(pl):	Biblioteka wsp�dzielona gnokii
Group:		Libraries
Conflicts:	gnokii < 1:0.5.10-0.2

%description -n libgnokii
A gnokii shared library

%description -n libgnokii -l pl
Biblioteka wsp�dzielona gnokii

%package -n libgnokii-devel
Summary:	libgnokii heades files
Summary(pl):	Pliki nag��wkowe biblioteki libgnokii
Group:		Development/Libraries
Requires:	libgnokii = %{epoch}:%{version}-%{release}
Requires:	XFree86-devel
Requires:	bluez-libs-devel >= 2.8-2
Obsoletes:	gnokii-devel

%description -n libgnokii-devel
libgnokii header files.

%description -n libgnokii-devel -l pl
Pliki nag��wkowe biblioteki libgnokii.

%package -n libgnokii-static
Summary:	Static libgnoki library
Summary(pl):	Statyczna biblioteka libgnokii
Group:		Development/Libraries
Requires:	libgnokii-devel = %{epoch}:%{version}-%{release}
Obsoletes:	gnokii-devel

%description -n libgnokii-static
Static version of libgnokii library.

%description -n libgnokii-static -l pl
Statyczna wersja biblioteki libgnokii.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -rf autom4te.cache
%{__gettextize}
%{__libtoolize}
%{__autoheader}
%{__aclocal} -I m4
%{__autoconf}
%configure \
	--enable-security \
	--with-xgnokiidir=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir}/{x,}gnokii} \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_pixmapsdir},%{_desktopdir}}

%{__make} install install-docs \
	DESTDIR=$RPM_BUILD_ROOT

install Docs/sample/gnokiirc $RPM_BUILD_ROOT%{_sysconfdir}/gnokiirc

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

# do not complain about unpackaged files (we package them with %%doc anyway)
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}

# move xgnokii manpage into proper place
mv -f  $RPM_BUILD_ROOT{%{_prefix}/man,%{_mandir}}/man1/xgnokii.1x

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libgnokii -p /sbin/ldconfig
%postun -n libgnokii -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Docs/{CREDITS,DataCalls-QuickStart,README*,Bugs,FAQ,*.txt,protocol}
%doc Docs/{sample/{gnokiirc,ppp*,ringtone,vCalendar,vCard},gnokii-{ir-howto,IrDA-Linux}}
%doc TODO ChangeLog MAINTAINERS
%attr(755,root,root) %{_bindir}/gnokii
%attr(755,root,root) %{_bindir}/todologo
%attr(755,root,root) %{_bindir}/sendsms
%attr(755,root,root) %{_bindir}/ppm2nokia
%attr(755,root,root) %{_sbindir}/gnokiid
%attr(755,root,root) %{_sbindir}/mgnokiidev
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/gnokiirc
%{_mandir}/man1/[!x]*
%{_mandir}/man8/*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xgnokii
%dir %{_datadir}/xgnokii
%{_libdir}/xgnokii
%{_datadir}/xgnokii/xpm
%{_datadir}/xgnokii/help
%{_desktopdir}/gnokii.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/xgnokii.1x*

%files -n libgnokii
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnokii.so.*.*

%files -n libgnokii-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnokii.so
%{_libdir}/libgnokii.la
%{_includedir}/*.h
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files -n libgnokii-static
%defattr(644,root,root,755)
%{_libdir}/libgnokii.a
