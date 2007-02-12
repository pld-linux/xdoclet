Summary:	XDoclet - a code generation engine for Java
Summary(pl.UTF-8):   XDoclet - silnik generowania kodu w Javie
Name:		xdoclet
Version:	1.2
Release:	1
License:	BSD
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/xdoclet/%{name}-bin-%{version}.tgz
# Source0-md5:	5152c5fdd07cf8ca37e0a8835463710d
Source1:	http://dl.sourceforge.net/xdoclet/%{name}-base-locale-%{version}.jar
# Source1-md5:	b919d7fd36822797497b75734f1e7b08
URL:		http://xdoclet.sourceforge.net/
BuildRequires:	jdk
BuildRequires:	ant
BuildRequires:	maven
Requires:	jdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XDoclet is an extended Javadoc Doclet engine. It's a generic Java tool
that lets you create custom Javadoc @tags and based on those @tags
generate source code or other files.

%description -l pl.UTF-8
XDoclet to rozszerzony silnik Javadoc Doclet. Jest generycznym
narzędziem Javy pozwalającym tworzyć własne @tagi Javadoc i na ich
podstawie generować kod źródłowy lub inne pliki.

%package doc
Summary:	Online manual for xdoclet
Summary(pl.UTF-8):   Dokumentacja online do xdoclet
Group:		Documentation

%description doc
Documentation for xdoclet - a code generation engine for Java.

%description doc -l pl.UTF-8
Dokumentacja do xdoclet - silnika generowania kodu w Javie.

%prep
%setup -q
unzip %{SOURCE1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xdoclet

cp -a lib $RPM_BUILD_ROOT%{_datadir}/xdoclet
cp -a xdoclet/ant $RPM_BUILD_ROOT%{_datadir}/xdoclet
cp -a xdoclet/loader $RPM_BUILD_ROOT%{_datadir}/xdoclet
cp -a xdoclet/modules $RPM_BUILD_ROOT%{_datadir}/xdoclet
cp -a xdoclet/tagshandler $RPM_BUILD_ROOT%{_datadir}/xdoclet
cp -a xdoclet/template $RPM_BUILD_ROOT%{_datadir}/xdoclet
cp -a xdoclet/util $RPM_BUILD_ROOT%{_datadir}/xdoclet
install xdoclet/*.properties $RPM_BUILD_ROOT%{_datadir}/xdoclet

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/xdoclet
%{_datadir}/xdoclet/lib
%{_datadir}/xdoclet/ant
%{_datadir}/xdoclet/loader
%{_datadir}/xdoclet/modules
%{_datadir}/xdoclet/tagshandler
%{_datadir}/xdoclet/template
%{_datadir}/xdoclet/util
%{_datadir}/xdoclet/*.properties

%files doc
%defattr(644,root,root,755)
%doc docs
