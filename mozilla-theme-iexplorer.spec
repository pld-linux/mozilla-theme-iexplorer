Summary:        Simulation of Internet Exporer 6.0 apperance
Summary(pl):    Symulacja wyg³±du Internet Explorera 6.0
Name:           mozilla-theme-iexplorer
Version:        1.0
Release:        1
License:        GPL
Group:          X11/Applications/Networking
Source0:        http://downloads.mozdev.org/themes/ieskin.jar
Source1:        ieskin-installed-chrome.txt
URL:            http://www0.mozdev.org/themes/skins/ie.html
Requires:       mozilla >= 1.0
BuildRoot:      %{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome
%define		_realname	ieskin

%description
%description -l pl
Temat dok³adnie symuluje wygl±d Internet Explorera 6.0 z MS Windows.

%prep
%setup -q -c -T
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt |grep -v "%{_realname}.jar" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
