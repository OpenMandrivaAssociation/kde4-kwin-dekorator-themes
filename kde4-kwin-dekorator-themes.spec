Name:		kde4-kwin-dekorator-themes
Summary:	Themes for deKorator for KDE 4
Version:	0.2
Release:	2
Group:		Graphical desktop/KDE
License:	GPL
URL:		http://www.kde-look.org/index.php?xcontentmode=21
Source0:	103545-S_Dark-0.1-theme.tar.gz
Source1:	31587-Plastic-theme.tar.bz2
Source2:	31720-Area-51.tar.bz2
Source3:	31740-Area-51-Lte.tar.bz2
Source4:	39007-Aero_Glass-theme.tar.gz
Source5:	56664-kore-theme.tar.gz
Source6:	73236-Golden_Wood.tar.gz
Source7:	90763-REDMOND-NORMA-theme.tar.gz
Source8:	beo-theme.tar.bz2
Source9:	137696-Vectorcell2b-theme.tar.gz
Source10:	148329-winclassic-theme.tar.gz
BuildRequires:	kde4-macros
BuildArch:	noarch

%description
Themes for deKorator pack. Includes:
-S_Dark 0.1
-Plastic
-Area-51
-Area-51-Lte
-Aero_Glass
-Kore
-Golden Wood Original
-Golden Wood Thin
-Redmond Norma (Vista)
-Beo
-Win Classic 1.0
-Vectorcell2 0.1

Get more themes at kde-look.org if you want.

%prep
%setup -q -T -c -n %{name}-%{version} -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10

%build

%install
mkdir -p %{buildroot}%{_kde_appsdir}/deKorator/themes
cp -R S_Dark-0.1-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
cp -R Plastic-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
cp -R Area-51 %{buildroot}%{_kde_appsdir}/deKorator/themes/Area-51-theme
cp -R Area-51-Lte %{buildroot}%{_kde_appsdir}/deKorator/themes/Area-51-Lte-theme
cp -R Aero_Glass-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
cp -R kore-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
cp -R Golden\ Wood/golden-wood-thin %{buildroot}%{_kde_appsdir}/deKorator/themes/golden-wood-thin-theme
cp -R Golden\ Wood/golden-wood\ original %{buildroot}%{_kde_appsdir}/deKorator/themes/golden-wood-original-theme
cp -R vista-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
cp -R beo-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
cp -R Vectorcell2b-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
cp -R winclassic-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/

cd %{buildroot}%{_kde_appsdir}/deKorator/themes/Area-51-theme
mv Buttons buttons
mv Deco deco
mv Masks masks
cd buttons
mkdir -p hover normal press
cp buttonClose.png buttonMax.png buttonMin.png normal
cp buttonClose.png hover/buttonCloseHover.png
cp buttonMax.png hover/buttonMaxHover.png
cp buttonMin.png hover/buttonMinHover.png
mv buttonClose.png press/buttonClosePress.png
mv buttonMax.png press/buttonMaxPress.png
mv buttonMin.png press/buttonMinPress.png

cd %{buildroot}%{_kde_appsdir}/deKorator/themes/Area-51-Lte-theme
mv Buttons buttons
mv Deco deco
mv Masks masks
cd buttons
mkdir -p hover normal press
cp buttonClose.png buttonMax.png buttonMin.png normal
cp buttonClose.png hover/buttonCloseHover.png
cp buttonMax.png hover/buttonMaxHover.png
cp buttonMin.png hover/buttonMinHover.png
mv buttonClose.png press/buttonClosePress.png
mv buttonMax.png press/buttonMaxPress.png
mv buttonMin.png press/buttonMinPress.png

cd %{buildroot}%{_kde_appsdir}/deKorator/themes
chmod 755 Aero_Glass-theme
cd Aero_Glass-theme
chmod -R 755 *

%files
%defattr(644,root,root,755)
%{_kde_appsdir}/deKorator/themes/*

%changelog
* Tue Feb 28 2012 Andrey Bondrov <abondrov@mandriva.org> 0.2-1mdv2011.0
+ Revision: 781299
- imported package kde4-kwin-dekorator-themes


* Tue Feb 28 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 0.2-1mdv2010.2
- Add Win Classic 1.0 and Vectorcell2 0.1 themes

* Sun Jul 11 2010 Andrey Bondrov <bondrov@math.dvgu.ru> 0.1-69.2mib2010.1
- Add kde4-macros to BuildRequires

* Wed May 13 2009 Andrey Bondrov <bondrov@math.dvgu.ru> 0.1-69.1mib2009.1
- First release for MIB users
- MIB (Mandriva Italia Backport) - http://mib.pianetalinux.org/

