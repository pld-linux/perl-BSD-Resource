%include	/usr/lib/rpm/macros.perl
%define		pdir	BSD
%define		pnam	Resource
Summary:	Perl module with BSD process resource limit and priority functions
Summary(cs):	Funkce pro BSD limity zdrojù a priority procesù
Summary(da):	BSD-procesresursegrænse- og -prioritetsfunktioner
Summary(de):	Funktionen zum Einstellen von Einschränkungen und Prioritäten der Ressourcen des BSD-Prozesses
Summary(es):	Funciones de prioridad y limite de recusros del proceso BSD
Summary(fr):	Limite de ressource de processus BSD et fonctions prioritaires
Summary(it):	Impostazione dei limiti e delle priorità delle risorse del processo BSD
Summary(ja):	BSD¤Î¥×¥í¥»¥¹¥ê¥½¡¼¥¹¤ÎÀ©¸Â¤ÈÍ¥ÀèÅÙ¤Îµ¡Ç½
Summary(ko):	BSD ÇÁ·Î¼¼½º ÀÚ¿ø ÇÑ°è¿Í ¿ì¼± ¼øÀ§ ÇÔ¼ö
Summary(pl):	Modu³ Perla z funkcjami BSD obs³uguj±cymi limity zasobów dla procesów
Summary(pt):	Funções de limitação de recursos e prioridades dos processos do BSD
Summary(pt_BR):	Funções de limitação de recursos e prioridades dos processos do BSD
Summary(sv):	BSD-processresursgräns- och -prioritetsfunktioner
Summary(tr):	BSD süreç özkaynak sýnýrý ve önceliði iþlevleri
Summary(zh_CN):	BSD ½ø³Ì×ÊÔ´ÏÞÖÆºÍÓÅÏÈ¼¶º¯Êý
Name:		perl-BSD-Resource
Version:	1.22
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6b63e4a0164e65f510e3b2dfbfd93090
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl extension implements the BSD process resource limit
functions (getrusage(), getrlimit(), setrlimit()) and the BSD process
priority functions. These are available also via core Perl but here we
do more tricks so that the PRIO_* are available (getpriority(),
setpriority()).

%description -l cs
Modul poskytující rozhraní pro testování a nastavování limitù zdrojù a
priorit procesu.

%description -l da
Et modul som leverer en grænseflade til at teste og sætte
procesbegrænsninger og prioriteter.

%description -l de
Ein Modul mit einem Interface für das Prüfen und Einstellen von
Prozesseinschränkgungen und -prioritäten.

%description -l es
Módulo que proporciona una interfaz para chequear y configurar los
límites del proceso y las prioridades.

%description -l fr
Module fournissant une interface pour tester et établir les limites de
processus et les priorités.

%description -l it
Modulo che offre un'interfaccia per testare e impostare i limiti e le
priorità dei processi.

%description -l ja
¥×¥í¥»¥¹¤ÎÀ©¸Â¤ÈÍ¥ÀèÅÙ¤ò¥Æ¥¹¥È¤·ÀßÄê¤¹¤ë°Ù¤Î¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹¤òÄó¶¡¤¹¤ë
¥â¥¸¥å¡¼¥ë¤Ç¤¹¡£

%description -l ko
ÇÁ·Î¼¼½º ÇÑ°è¿Í ¿ì¼± ¼øÀ§¸¦ ¼³Á¤ÇÏ°í ½ÃÇèÇÏ´Âµ¥ »ç¿ëµÇ´Â ÀÎÅÍÆäÀÌ½º¸¦
Á¦°øÇÏ´Â ¸ðµâ.

%description -l pl
To rozszerzenie Perle jest implementacj± funkcji BSD dotycz±cych
limitów zasobów dla procesów (getrusage(), getrlimit(), setrlimit())
oraz funkcji BSD zwi±zanych z priorytetami procesów. S± one dostêpne
tak¿e z podstawowego Perla, ale ten modu³ pozwala na wiêcej sztuczek,
bo dostêpne s± PRIO_* (getpriority(), setpriority()).

%description -l pt
Um módulo que oferece uma interface para testar e definir os limites e
prioridades dos processos.

%description -l pt_BR
Um módulo que oferece uma interface para testar e definir os limites e
prioridades dos processos.

%description -l sv
En modul som tillhandahåller ett gränssnitt för att testa och sätta
processbegränsningar och prioriteter.

%description -l zh_CN
Îª²âÊÔºÍÉèÖÃ½ø³ÌÏÞ¶ÈºÍÓÅÏÈ¼¶¶øÌá¹©µÄÄ£¿é¡£

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/BSD/Resource.pm
%dir %{perl_vendorarch}/auto/BSD/Resource
%{perl_vendorarch}/auto/BSD/Resource/*.al
%{perl_vendorarch}/auto/BSD/Resource/autosplit.ix
%{perl_vendorarch}/auto/BSD/Resource/Resource.bs
%attr(755,root,root) %{perl_vendorarch}/auto/BSD/Resource/Resource.so
%{_mandir}/man3/*
