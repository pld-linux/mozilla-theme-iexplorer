Summary:	Simulation of Internet Exporer 6.0 appearance
Summary(pl):	Symulacja wygl±du Internet Explorera 6.0
Name:		mozilla-theme-iexplorer
%define		_realname	ieskin
Version:	1.3
Release:	5
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/themes/%{_realname}%{version}.xpi
# Source0-md5:	fad61f903a906228a3705ff05b5bbf37
# Source0-size:	223001
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/skins/ie.html
BuildRequires:	perl-base
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	textutils
Requires:	mozilla >= 5:1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
This theme is exact simulation of MS Internet Explorer 6.0 appearance.

%description -l pl
Motyw dok³adnie symuluje wygl±d Internet Explorera 6.0 z MS Windows.

%prep
%setup -c
unzip -o ieskin.jar
rm -f ieskin.jar

%build
perl -pi -e 's/(skinVersion=)"1\.[0-9]"/$1"1.5"/' contents.rdf
find -name "*.css" | xargs perl -pi -e 's/:-moz-/::-moz-/'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

zip -r $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar *
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
