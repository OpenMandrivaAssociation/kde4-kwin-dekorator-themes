Name:		kde4-kwin-dekorator-themes
Summary:	Themes for deKorator for KDE 4
Version:	0.2
Release:	%mkrel 1
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
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_kde_appsdir}/deKorator/themes
%__cp -R S_Dark-0.1-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
%__cp -R Plastic-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
%__cp -R Area-51 %{buildroot}%{_kde_appsdir}/deKorator/themes/Area-51-theme
%__cp -R Area-51-Lte %{buildroot}%{_kde_appsdir}/deKorator/themes/Area-51-Lte-theme
%__cp -R Aero_Glass-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
%__cp -R kore-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
%__cp -R Golden\ Wood/golden-wood-thin %{buildroot}%{_kde_appsdir}/deKorator/themes/golden-wood-thin-theme
%__cp -R Golden\ Wood/golden-wood\ original %{buildroot}%{_kde_appsdir}/deKorator/themes/golden-wood-original-theme
%__cp -R vista-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
%__cp -R beo-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
%__cp -R Vectorcell2b-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/
%__cp -R winclassic-theme %{buildroot}%{_kde_appsdir}/deKorator/themes/


cd %{buildroot}%{_kde_appsdir}/deKorator/themes/Area-51-theme
%__mv Buttons buttons
%__mv Deco deco
%__mv Masks masks
cd buttons
%__mkdir_p hover normal press
%__cp buttonClose.png buttonMax.png buttonMin.png normal
%__cp buttonClose.png hover/buttonCloseHover.png
%__cp buttonMax.png hover/buttonMaxHover.png
%__cp buttonMin.png hover/buttonMinHover.png
%__mv buttonClose.png press/buttonClosePress.png
%__mv buttonMax.png press/buttonMaxPress.png
%__mv buttonMin.png press/buttonMinPress.png

cd %{buildroot}%{_kde_appsdir}/deKorator/themes/Area-51-Lte-theme
%__mv Buttons buttons
%__mv Deco deco
%__mv Masks masks
cd buttons
%__mkdir_p hover normal press
%__cp buttonClose.png buttonMax.png buttonMin.png normal
%__cp buttonClose.png hover/buttonCloseHover.png
%__cp buttonMax.png hover/buttonMaxHover.png
%__cp buttonMin.png hover/buttonMinHover.png
%__mv buttonClose.png press/buttonClosePress.png
%__mv buttonMax.png press/buttonMaxPress.png
%__mv buttonMin.png press/buttonMinPress.png

cd %{buildroot}%{_kde_appsdir}/deKorator/themes
%__chmod 755 Aero_Glass-theme
cd Aero_Glass-theme
%__chmod -R 755 *

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_kde_appsdir}/deKorator/themes/*

