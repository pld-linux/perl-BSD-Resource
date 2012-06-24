%include	/usr/lib/rpm/macros.perl
%define		pdir	BSD
%define		pnam	Resource
Summary:	Perl module with BSD process resource limit and priority functions
Summary(cs):	Funkce pro BSD limity zdroj� a priority proces�
Summary(da):	BSD-procesresursegr�nse- og -prioritetsfunktioner
Summary(de):	Funktionen zum Einstellen von Einschr�nkungen und Priorit�ten der Ressourcen des BSD-Prozesses
Summary(es):	Funciones de prioridad y limite de recusros del proceso BSD
Summary(fr):	Limite de ressource de processus BSD et fonctions prioritaires
Summary(it):	Impostazione dei limiti e delle priorit� delle risorse del processo BSD
Summary(ja):	BSD�Υץ����꥽���������¤�ͥ���٤ε�ǽ
Summary(ko):	BSD ���μ��� �ڿ� �Ѱ�� �켱 ���� �Լ�
Summary(pl):	Modu� Perla z funkcjami BSD obs�uguj�cymi limity zasob�w dla proces�w
Summary(pt):	Fun��es de limita��o de recursos e prioridades dos processos do BSD
Summary(pt_BR):	Fun��es de limita��o de recursos e prioridades dos processos do BSD
Summary(sv):	BSD-processresursgr�ns- och -prioritetsfunktioner
Summary(tr):	BSD s�re� �zkaynak s�n�r� ve �nceli�i i�levleri
Summary(zh_CN):	BSD ������Դ���ƺ����ȼ�����
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
Modul poskytuj�c� rozhran� pro testov�n� a nastavov�n� limit� zdroj� a
priorit procesu.

%description -l da
Et modul som leverer en gr�nseflade til at teste og s�tte
procesbegr�nsninger og prioriteter.

%description -l de
Ein Modul mit einem Interface f�r das Pr�fen und Einstellen von
Prozesseinschr�nkgungen und -priorit�ten.

%description -l es
M�dulo que proporciona una interfaz para chequear y configurar los
l�mites del proceso y las prioridades.

%description -l fr
Module fournissant une interface pour tester et �tablir les limites de
processus et les priorit�s.

%description -l it
Modulo che offre un'interfaccia per testare e impostare i limiti e le
priorit� dei processi.

%description -l ja
�ץ��������¤�ͥ���٤�ƥ��Ȥ����ꤹ��٤Υ��󥿡��ե��������󶡤���
�⥸�塼��Ǥ���

%description -l ko
���μ��� �Ѱ�� �켱 ������ �����ϰ� �����ϴµ� ���Ǵ� �������̽���
�����ϴ� ���.

%description -l pl
To rozszerzenie Perle jest implementacj� funkcji BSD dotycz�cych
limit�w zasob�w dla proces�w (getrusage(), getrlimit(), setrlimit())
oraz funkcji BSD zwi�zanych z priorytetami proces�w. S� one dost�pne
tak�e z podstawowego Perla, ale ten modu� pozwala na wi�cej sztuczek,
bo dost�pne s� PRIO_* (getpriority(), setpriority()).

%description -l pt
Um m�dulo que oferece uma interface para testar e definir os limites e
prioridades dos processos.

%description -l pt_BR
Um m�dulo que oferece uma interface para testar e definir os limites e
prioridades dos processos.

%description -l sv
En modul som tillhandah�ller ett gr�nssnitt f�r att testa och s�tta
processbegr�nsningar och prioriteter.

%description -l zh_CN
Ϊ���Ժ����ý����޶Ⱥ����ȼ����ṩ��ģ�顣

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
