Summary:	Linux/Unix tool suite for Nokia mobile phones
Summary(pl):	Linuksowy/Uniksowy zestaw narzêdzi dla telefonów komórkowych Nokia
Name:		gnokii
Version:	0.3.3_pre7
Release:	1
License:	GPL
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source0:	ftp://ftp.linux.cz/pub/linux/people/pavel_janik/Gnokii/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.gnokii.org
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnokii is a Linux/Unix tool suite and (eventually) modem/fax driver
for Nokia's mobile phones, released under the GPL.

%description -l pl
Gnokii jest zestawem narzêdzi dla Linuksa/Uniksa, oraz (ewentualnie)
sterownikiem modemu/faxu dla telefonów komórkowych Nokia, dostêpnym na
licencji GPL.

%package X11
Summary:	Graphical Linux/Unix tool suite for Nokia mobile phones.
Summary(pl):	Zestaw narzêdzi z graficznym interfejsem dla telefonów komórkowych Nokia.
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Requires:	%{name} = %{version}

%description X11
Xgnokii is graphical Linux/Unix tool suite for Nokia's mobile phones.
It allows you to edit your contacts book, send/read SMS's from/in
computer and more other features.

%description X11 -l pl
Gnokii-X11 jest zestawem narzêdzi z graficznym interfejsem u¿ytkownika
do pracy z telefonami komórkowymi Nokia. Pozwalaj± one na edytowanie
spisu telefonów, wysy³anie/czytanie wiadomo¶ci SMS i wiele innych
rzeczy.

%prep
%setup -q
%patch0 -p1

%build
LDFLAGS="-s"; export LDFLAGS
aclocal
autoconf
%configure \
	--enable-security
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir}/gnokii} \
	$RPM_BUILD_ROOT{%{_prefix}/X11R6/{bin,lib/xgnokii},%{_sysconfdir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install Docs/sample.gnokiirc $RPM_BUILD_ROOT%{_sysconfdir}/gnokiirc

gzip -9nf Docs/{CREDITS,DataCalls-QuickStart,README{,-{3810,6110}}} \
	Docs/{sample.gnokiirc,gnokii-ir-howto} \
	TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Docs/*.gz Docs/gnokii.nol
%doc *.gz
%attr(755,root,root) %{_bindir}/gnokii
%attr(755,root,root) %{_sbindir}/gnokiid
%attr(755,root,root) %{_sbindir}/mgnokiidev
%config(noreplace) %{_sysconfdir}/gnokiirc

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/xgnokii
%attr(755,root,root) %{_prefix}/X11R6/bin/xlogos
%{_prefix}/X11R6/lib/xgnokii/help/en_US
%{_prefix}/X11R6/lib/xgnokii/xpm
