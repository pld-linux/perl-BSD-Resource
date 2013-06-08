#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
# hgw why it doesn't work on builders... temporary disables.
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	BSD
%define		pnam	Resource
Summary:	Perl module with BSD process resource limit and priority functions
Summary(cs.UTF-8):	Funkce pro BSD limity zdrojů a priority procesů
Summary(da.UTF-8):	BSD-procesresursegrænse- og -prioritetsfunktioner
Summary(de.UTF-8):	Funktionen zum Einstellen von Einschränkungen und Prioritäten der Ressourcen des BSD-Prozesses
Summary(es.UTF-8):	Funciones de prioridad y limite de recusros del proceso BSD
Summary(fr.UTF-8):	Limite de ressource de processus BSD et fonctions prioritaires
Summary(it.UTF-8):	Impostazione dei limiti e delle priorità delle risorse del processo BSD
Summary(ja.UTF-8):	BSDのプロセスリソースの制限と優先度の機能
Summary(ko.UTF-8):	BSD 프로세스 자원 한계와 우선 순위 함수
Summary(pl.UTF-8):	Moduł Perla z funkcjami BSD obsługującymi limity zasobów dla procesów
Summary(pt.UTF-8):	Funções de limitação de recursos e prioridades dos processos do BSD
Summary(pt_BR.UTF-8):	Funções de limitação de recursos e prioridades dos processos do BSD
Summary(sv.UTF-8):	BSD-processresursgräns- och -prioritetsfunktioner
Summary(tr.UTF-8):	BSD süreç özkaynak sınırı ve önceliği işlevleri
Summary(zh_CN.UTF-8):	BSD 进程资源限制和优先级函数
Name:		perl-BSD-Resource
Version:	1.2904
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/BSD/JHI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e6b31521b11a27b8266141a7b15f58a8
URL:		http://search.cpan.org/dist/BSD-Resource/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl extension implements the BSD process resource limit
functions (getrusage(), getrlimit(), setrlimit()) and the BSD process
priority functions. These are available also via core Perl but here we
do more tricks so that the PRIO_* are available (getpriority(),
setpriority()).

%description -l cs.UTF-8
Modul poskytující rozhraní pro testování a nastavování limitů zdrojů a
priorit procesu.

%description -l da.UTF-8
Et modul som leverer en grænseflade til at teste og sætte
procesbegrænsninger og prioriteter.

%description -l de.UTF-8
Ein Modul mit einem Interface für das Prüfen und Einstellen von
Prozesseinschränkgungen und -prioritäten.

%description -l es.UTF-8
Módulo que proporciona una interfaz para chequear y configurar los
límites del proceso y las prioridades.

%description -l fr.UTF-8
Module fournissant une interface pour tester et établir les limites de
processus et les priorités.

%description -l it.UTF-8
Modulo che offre un'interfaccia per testare e impostare i limiti e le
priorità dei processi.

%description -l ja.UTF-8
プロセスの制限と優先度をテストし設定する為のインターフェイスを提供する
モジュールです。

%description -l ko.UTF-8
프로세스 한계와 우선 순위를 설정하고 시험하는데 사용되는 인터페이스를
제공하는 모듈.

%description -l pl.UTF-8
To rozszerzenie Perla jest implementacją funkcji BSD dotyczących
limitów zasobów dla procesów (getrusage(), getrlimit(), setrlimit())
oraz funkcji BSD związanych z priorytetami procesów. Są one dostępne
także z podstawowego Perla, ale ten moduł pozwala na więcej sztuczek,
bo dostępne są PRIO_* (getpriority(), setpriority()).

%description -l pt.UTF-8
Um módulo que oferece uma interface para testar e definir os limites e
prioridades dos processos.

%description -l pt_BR.UTF-8
Um módulo que oferece uma interface para testar e definir os limites e
prioridades dos processos.

%description -l sv.UTF-8
En modul som tillhandahåller ett gränssnitt för att testa och sätta
processbegränsningar och prioriteter.

%description -l zh_CN.UTF-8
为测试和设置进程限度和优先级而提供的模块。

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_mandir}/man3/BSD::Resource.3pm*
