
%define base_name	kde-icons
%define theme_name      nuoveXT
%define version		1.6
%define name		%{base_name}-%{theme_name}
%define release		%mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	New everaldo crystal icons set
License:	GPL
Group:		Graphical desktop/KDE
Source:		http://nuovext.pwsp.net/files/%{theme_name}-kde-%{version}.tar.bz2
URL:		https://nuovext.pwsp.net/
Requires:	kdebase3-progs
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot



%description
nuoveXT is an icon theme for KDE.

The goal of nuoveXT is to provide 
a very complete set of icons for both Gnome and KDE. 
All icons are made entirely with Inkscape. 
A few icons was based or found in the Open Clip Art Library. 

%prep
rm -rf %buildroot
%setup -q -n %{theme_name}-kde-%{version}

%build

%install
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}/16x16
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}/22x22
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}/32x32
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}/48x48
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}/64x64
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}/128x128
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}/extras
cp -fr * %buildroot%{_iconsdir}/%{theme_name}/
cp -f 16x16/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}/16x16/apps/menuk-mdk.png
cp -f 16x16/apps/background.png %buildroot%_iconsdir/%{theme_name}/16x16/apps/desktop-mdk.png
cp -f 16x16/apps/kfm_home-alt.png %buildroot%_iconsdir/%{theme_name}/16x16/apps/home-mdk.png
cp -f 16x16/apps/kcmsound.png %buildroot%_iconsdir/%{theme_name}/16x16/apps/kmix.png
cp -f 16x16/apps/messenger.png %buildroot%_iconsdir/%{theme_name}/16x16/apps/kopete.png
cp -f 22x22/apps/kcmsound.png %buildroot%_iconsdir/%{theme_name}/22x22/apps/kmix.png
cp -f 22x22/apps/messenger.png %buildroot%_iconsdir/%{theme_name}/22x22/apps/kopete.png
cp -f 32x32/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}/32x32/apps/menuk-mdk.png
cp -f 32x32/apps/background.png %buildroot%_iconsdir/%{theme_name}/32x32/apps/desktop-mdk.png
cp -f 32x32/apps/kfm_home-alt.png %buildroot%_iconsdir/%{theme_name}/32x32/apps/home-mdk.png
cp -f 32x32/apps/kcmsound.png %buildroot%_iconsdir/%{theme_name}/32x32/apps/kmix.png
cp -f 32x32/apps/messenger.png %buildroot%_iconsdir/%{theme_name}/32x32/apps/kopete.png
cp -f 48x48/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}/48x48/apps/menuk-mdk.png
cp -f 48x48/apps/background.png %buildroot%_iconsdir/%{theme_name}/48x48/apps/desktop-mdk.png
cp -f 48x48/apps/kfm_home-alt.png %buildroot%_iconsdir/%{theme_name}/48x48/apps/home-mdk.png
cp -f 48x48/apps/kcmsound.png %buildroot%_iconsdir/%{theme_name}/48x48/apps/kmix.png
cp -f 48x48/apps/messenger.png %buildroot%_iconsdir/%{theme_name}/48x48/apps/kopete.png
cp -f 64x64/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}/64x64/apps/menuk-mdk.png
cp -f 64x64/apps/background.png %buildroot%_iconsdir/%{theme_name}/64x64/apps/desktop-mdk.png
cp -f 64x64/apps/kfm_home-alt.png %buildroot%_iconsdir/%{theme_name}/64x64/apps/home-mdk.png
cp -f 128x128/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}/128x128/apps/menuk-mdk.png
cp -f 128x128/apps/background.png %buildroot%_iconsdir/%{theme_name}/128x128/apps/desktop-mdk.png
cp -f 128x128/apps/kfm_home-alt.png %buildroot%_iconsdir/%{theme_name}/128x128/apps/home-mdk.png
cp -f extras/*.png %buildroot%_iconsdir/%{theme_name}/extras/
%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGELOG GPL
%{_iconsdir}/%{theme_name}/*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6-7mdv2011.0
+ Revision: 619900
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.6-6mdv2010.0
+ Revision: 438082
- rebuild

* Sun Mar 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.6-5mdv2009.1
+ Revision: 360336
- Fix Requires

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.6-4mdv2009.0
+ Revision: 247623
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.6-2mdv2008.1
+ Revision: 107288
- Fix Requires (kdebase-progs is a better require)
- import kde-icons-nuoveXT


* Tue Jul 11 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.6-2mdv2007.0
- Rebuild for new extension

* Thu Apr 06 2006 Sebastien Savarin <plouf@mandriva.org> 1.6-1mdk
- New release 1.6

* Thu Nov 17 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.5-2mdk
- fix description (aka describe this package, not inkscape)

* Wed Nov 16 2005 Sebastien Savarin <plouf@mandriva.org> 1.5-1mdk
- First Mandriva Linux release
