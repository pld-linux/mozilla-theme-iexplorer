Summary:	Simulation of Internet Exporer 6.0 appearance
Summary(pl):	Symulacja wygl±du Internet Explorera 6.0
Name:		mozilla-theme-iexplorer
%define		_realname	ieskin
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://pages.prodigy.net/zzxc/%{_realname}/%{_realname}%{version}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/skins/ie.html
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
This theme is exact simulation of MS Internet Explorer 6.0 appearance.

%description -l pl
Motyw dok³adnie symuluje wygl±d Internet Explorera 6.0 z MS Windows.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} ieskin.jar -d $RPM_BUILD_ROOT%{_chromedir}
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
