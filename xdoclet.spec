Summary:	XDoclet is a code generation engine for Java
Summary(pl):	XDoclet to silnik generowania kodu w Javie
Name:		xdoclet
Version:	1.2
Release:	1
License:	BSD
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-bin-%{version}.tgz
# Source0-md5:	5152c5fdd07cf8ca37e0a8835463710d
Source1:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-base-locale-%{version}.jar
# Source1-md5:	b919d7fd36822797497b75734f1e7b08
URL:		http://xdoclet.sourceforge.net/
BuildRequires:	jdk
BuildRequires:	jakarta-ant
BuildRequires:	maven
Requires:	jdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XDoclet is an extended Javadoc Doclet engine. It's a generic Java tool
that lets you create custom Javadoc @tags and based on those @tags
generate source code or other files.

%description -l pl
XDoclet to rozszerzony silnik Javadoc Doclet. Jest generycznym
narzêdziem Javy pozwalaj±cym tworzyæ w³asne @tagi Javadoc i na ich
podstawie generowaæ kod ¼ród³owy lub inne pliki.

%package doc
Summary:	Online manual for xdoclet
Summary(pl):	Dokumentacja online do xdoclet
Group:		Documentation

%description doc
Documentation for xdoclet - a code generation engine for Java

%description doc -l pl
Dokumentacja do xdoclet - silnika generowania kodu w Javie

%prep
%setup -q -n %{name}-%{version}
unzip %{SOURCE1}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/xdoclet
mv lib $RPM_BUILD_ROOT%{_datadir}/xdoclet
mv xdoclet/ant $RPM_BUILD_ROOT%{_datadir}/xdoclet
mv xdoclet/loader $RPM_BUILD_ROOT%{_datadir}/xdoclet
mv xdoclet/modules $RPM_BUILD_ROOT%{_datadir}/xdoclet
mv xdoclet/tagshandler $RPM_BUILD_ROOT%{_datadir}/xdoclet
mv xdoclet/template $RPM_BUILD_ROOT%{_datadir}/xdoclet
mv xdoclet/util $RPM_BUILD_ROOT%{_datadir}/xdoclet
install xdoclet/*.properties $RPM_BUILD_ROOT%{_datadir}/xdoclet

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
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
