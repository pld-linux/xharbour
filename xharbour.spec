#
# Conditional build:
%bcond_with	static		# link all binaries with static libs
%bcond_with	adsrdd		# build ads RDD
%bcond_with	mysql		# build mysql lib
%bcond_with	pgsql		# build pgsql lib
%bcond_with	odbc		# build odbc lib
%bcond_with	hrbsh		# build /etc/profile.d/harb.sh (not necessary)
%bcond_without	x11		# do not build GTXVT and GTXWC
%bcond_without	gpm		# build GTSLN and GTCRS without GPM support
%bcond_without	gtsln		# do not build GTSLN
%bcond_without	nf		# do not build nanforum lib doesn't work now
#
# TODO:
# nf
# pprun
# - fix pt_BR (utf-8 broken by 8-bit copy-paste?)
#
Summary:	Backwards compatible Clipper Language compiler and preprocessor
Summary(pl):	Zgodny wstecz kompilator i preprocesor Clippera
Name:		xharbour
Version:	0.99.3
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Development/Languages
Source0:	http://files.xharbour.org/source/%{name}-%{version}.src.tar.gz
# Source0-md5:	7e660044656df06d98589da25285fc20
Source1:	http://files.xharbour.org/source/%{name}-%{version}.src.contrib.tar.gz
URL:		http://www.xharbour.org/
Requires:	%{name}-lib = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xHarbour is a CA-Clipper compatible compiler for multiple platforms.
This package includes a compiler, pre-processor, header files, virtual
machine and documentation.

See README.RPM in the documentation directory for information specific
to this RPM distribution.

%description -l pl
xHarbour to kompatybilny z jЙzykiem CA-Clipper kompilator rozwijany na
wielu rС©nych platformach. Ten pakiet zawiera kompilator, preprocesor,
pliki nagЁСwkowe, wirtualn╠ maszynЙ oraz dokumentacjЙ.

%description -l pt_BR
xHarbour ~B um compilador Clipper compativel para multiplas
plataformas. Esse pacote contem um compilador, um pr~B-processador,
arquivos de cabe~Galho uma maquina virtual e documenta~Gфo.

%description -l ru
xHarbour - многоплатформенный компилятор, совместимый с языком
CA-Clipper. Этот пакет содержит компилятор, препроцессор, файлы
заголовков, виртуальную машину и документацию.

%package lib
Summary:	Shared runtime libaries for xHarbour compiler
Summary(pl):	Dzielone bilioteki dla kompilatora xHarbour
Summary(ru):	Совместно используемые библиотеки для компилятора xHarbour
Group:		Libraries
# XXX: should be autodetected
Provides:	lib%{name}.so lib%{name}mt.so

%description lib
xHarbour is a Clipper compatible compiler. This package provides
xHarbour runtime shared libraries for programs linked dynamically.

%description lib -l pl
xHarbour to kompatybilny z jЙzykiem CA-Clipper kompilator. Ten pakiet
udostЙpnia dzielone bilioteki kompilatora xHarbour dla programСw
konsolidowanych dynamicznie.

%description lib -l pt_BR
xHarbour ~B um compilador compativel com o Clipper. Esse pacote
xHarbour provem as bibliotecas compartilhadas para programas linkados
dinamicamente.

%description lib -l ru
xHarbour - компилятор, совместимый с языком CA-Clipper. Этот пакет
содержит совместно используемые библиотеки xHarbour, необходимые для
работы динамически скомпонованных программ.

%package static
Summary:	Static runtime libaries for xHarbour compiler
Summary(pl):	Statyczne bilioteki dla kompilatora xHarbour
Summary(ru):	Статические библиотеки для компилятора xHarbour
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description static
xHarbour is a Clipper compatible compiler. This package provides
xHarbour static runtime libraries for static program linking.

%description static -l pl
xHarbour to kompatybilny z jЙzykiem CA-Clipper kompilator. Ten pakiet
udostЙpnia statyczne bilioteki dla kompilatora xHarbour niezbЙdne do
statycznej konsolidacji programСw.

%description static -l pt_BR
xHarbour ~B um compilador compativel com o clippe. Esse pacote
xHarbour provem as bibliotecas de run time staticas para linkagem dos
os programas

%description static -l ru
xHarbour - компилятор, совместимый с языком CA-Clipper. Этот пакет
содержит статические библиотеки компилятора xHarbour, необходимые для
статической компоновки программ.

%package contrib
Summary:	Contrib runtime libaries for xHarbour compiler
Summary(pl):	Bilioteki z drzewa contrib dla kompilatora xHarbour
Summary(pt_BR):	Libs contrib para xHarbour
Summary(ru):	Библиотеки из дерева contrib для компилятора xHarbour
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description contrib
xHarbour is a Clipper compatible compiler. This package provides
xHarbour contrib libraries for program linking.

%description contrib -l pl
xHarbour to kompatybilny z jЙzykiem CA-Clipper kompilator. Ten pakiet
udostЙpnia statyczne bilioteki z drzewa contrib dla kompilatora
xHarbour.

%description contrib -l pt_BR
xHarbour ~B um compilador compativel com o clippe. Esse pacote
xHarbour provem as bibliotecas contrib para linkagem dos programas.

%description contrib -l ru
xHarbour - компилятор, совместимый с языком CA-Clipper. Этот пакет
содержит статические библиотеки xHarbour из дерева contrib.

%package pp
Summary:	Clipper/Harbour/xBase compatible Pre-Processor, DOT prompt and interpreter
Summary(pl):	Kompatybilny z Clipper/Harbour/xBase Preprocesor i interpreter
Summary(ru):	Совместимый с Clipper/Harbour/xBase препроцессор и интерпретатор
License:	GPL
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description pp
xHarbour is a Clipper compatible compiler. This package provides
xHarbour PP. It has 3 personalities which are tied tightly together.
1. What is supposed to be 100% Clipper compatible Pre-Processor (with
some extensions). 2. DOT prompt, which suppose to allow most of
Clipper syntax. 3. Finally, PP is a limited Clipper/Harbour/xBase
Interpreter. Subject to those same few limitations it can execute most
of Harbour syntax. You can write your own xBase scripts by adding to
your .prg files #!/usr/bin/pprun

%description pp -l pl
xHarbour to kompatybilny z jЙzykiem CA-Clipper kompilator. Ten pakiet
udostЙpnia xHarbour PP, ktСry daje trzy narzЙdzia w jednym. 1. W 100%
kompatybilny z Clipperem preprocesor (z pewnymi rozeszerzeniami) 2.
╕rodowisko DOT, w ktСrym mo©na u©ywaФ wiЙkszo╤ci skЁadni Clippera 3.
PP to tak©e nieco ograniczony interpreter Clippera. Z uwzglЙdnieniem
wspomnianych kilku ograniczeЯ potrafi on uruchomiФ wiЙkszo╤Ф skЁadni
Harbour. Mo©na napisaФ swСj wЁasny skrypt xBase dodaj╠c
"#!/usr/bin/pprun" do pliku .prg.

%description pp -l pt_BR
xHarbour ~B um compilador Clipper compativel. Esse pacote provem o
xHarbour PP. Ele tem 3 caracteristicas dependentes uma da outra. 1.
Que e supostamente ser um Pre-Processor 100% compativel com o Clipper
(com algumas extenssДes). 2. DOT prompt, que supostamente permite a
maioria das syntaxes do Clipper. 3. Finalmente, PP ~B um limitado
Interpretador Clipper/Harbour/xBase . Sujeito com algumas limita~GДes
que pode executar a maioria da syntaxe do Harbour. Voce pode escrever
seus proprios scritps em .prg ao adicionar as seus arquivos .prg
#!/usr/bin/pprun

%description pp -l ru
xHarbour - компилятор, совместимый с языком CA-Clipper. Этот пакет
содержит препроцессор xHarbour, который состоит из трех тесно
связанных частей. 1. 100%-совместимый с Clipper препроцессор (с
некоторыми расширениями). 2. DOT Prompt, в котором можно использовать
большинство конструкций Clipper. 3. Кроме того, PP - ограниченный
интерпретатор Clipper. За исключением нескольких описанных
ограничений, он может выполнять большинство конструкций Harbour. Можно
создавать собственные xBase-скрипты путем добавления в начало
.prg-файла строки: #!/usr/bin/pprun

%prep
%setup -q -b 1

%build
%if "%{platform}" == ""
%define platform %([ -f %{_sysconfdir}/pld-release ] && cat %{_sysconfdir}/pld-release|sed -e '/1/ !d' -e 's/[^0-9]//g' -e 's/^/pld/')
%endif

%define hb_pref  xhb
%define hb_arch  export HB_ARCHITECTURE=linux
%define hb_cc    export HB_COMPILER=gcc
%define hb_cflag export C_USR="-DHB_FM_STATISTICS_OFF -O3"
%define hb_lflag export L_USR=%{?with_static:-static}
%define hb_mt    export HB_MT=MT
%define hb_mgt   export HB_MULTI_GT=yes
%define hb_gt    export HB_GT_LIB=gtcrs
%define hb_gpm   export HB_GPM_MOUSE=%{?with_gpm:yes}
%define hb_sln   export HB_WITHOUT_GTSLN=%{!?with_gtsln:yes}
%define hb_x11   export HB_WITHOUT_X11=%{!?with_x11:yes}
%define hb_bdir  export HB_BIN_INSTALL=%{_bindir}
%define hb_idir  export HB_INC_INSTALL=%{_includedir}/%{name}
%define hb_ldir  export HB_LIB_INSTALL=%{_libdir}/%{name}
%define hb_opt   export HB_GTALLEG=%{?with_allegro:yes}
%define hb_cmrc  export HB_COMMERCE=no
%define hb_ctrb  %{?with_nf:libnf} %{?with_adsrdd:rdd_ads} %{?with_mysql:mysql} %{?with_pgsql:pgsql}
%define hb_env   %{hb_arch} ; %{hb_cc} ; %{hb_cflag} ; %{hb_lflag} ; %{hb_mt} ; %{hb_gt} ; %{hb_gpm} ; %{hb_sln} ; %{hb_x11} ; %{hb_mgt} ; %{hb_bdir} ; %{hb_idir} ; %{hb_ldir} ; %{hb_opt} ; %{hb_cmrc}

%define hb_host  www.xharbour.org
%define readme   README.RPM

%{hb_env}

%{__make}

# build contrib libraries
for l in %{hb_ctrb} ; do
	cd "contrib/$l"
	%{__make}
	cd ../..
done

%install
rm -rf $RPM_BUILD_ROOT
%{hb_env}

export _DEFAULT_BIN_DIR=$HB_BIN_INSTALL
export _DEFAULT_INC_DIR=$HB_INC_INSTALL
export _DEFAULT_LIB_DIR=$HB_LIB_INSTALL
export HB_BIN_INSTALL=$RPM_BUILD_ROOT/$HB_BIN_INSTALL
export HB_INC_INSTALL=$RPM_BUILD_ROOT/$HB_INC_INSTALL
export HB_LIB_INSTALL=$RPM_BUILD_ROOT/$HB_LIB_INSTALL

install -d $HB_BIN_INSTALL
install -d $HB_INC_INSTALL
install -d $HB_LIB_INSTALL

#./contrib/pgsql/linux/gcc/libhbpg.a
for l in %{hb_ctrb}
do
	cd "contrib/$l"
	%{__make} install
	cd ../..
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%doc ChangeLog
%doc doc/*.txt
#%doc doc/%{readme}
%doc doc/en/
%doc doc/es/

#%dir /etc/harbour
#%verify(not md5 mtime size) %config(noreplace) /etc/harbour.cfg
#%verify(not md5 mtime size) %config(noreplace) /etc/harbour/hb-charmap.def
%{?with_hrbsh:/etc/profile.d/harb.sh}

%attr(755,root,root) %{_bindir}/harbour
%attr(755,root,root) %{_bindir}/hb-mkslib
%attr(755,root,root) %{_bindir}/%{hb_pref}-build
%attr(755,root,root) %{_bindir}/%{hb_pref}cc
%attr(755,root,root) %{_bindir}/%{hb_pref}cmp
%attr(755,root,root) %{_bindir}/%{hb_pref}lnk
%attr(755,root,root) %{_bindir}/%{hb_pref}mk
%attr(755,root,root) %{_bindir}/gharbour
%attr(755,root,root) %{_bindir}/harbour-link
%attr(755,root,root) %{_bindir}/hbtest
%attr(755,root,root) %{_bindir}/hbrun
%attr(755,root,root) %{_bindir}/hbpp
%attr(755,root,root) %{_bindir}/hbmake
%attr(755,root,root) %{_bindir}/hbdict
%attr(755,root,root) %{_bindir}/hbdict_es_MX.hit
%attr(755,root,root) %{_bindir}/hbdict_it_IT.hit
%attr(755,root,root) %{_bindir}/hbdict_pl_PL.hit
%attr(755,root,root) %{_bindir}/hbdoc

%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/%{name}/libcodepage.a
%{_libdir}/%{name}/libcommon.a
%{_libdir}/%{name}/libdb*.a
%{_libdir}/%{name}/libdebug.a
%{_libdir}/%{name}/libfm*.a
%{_libdir}/%{name}/libgt*.a
%{_libdir}/%{name}/libhbtip*.a
%{?with_odbc:%{_libdir}/%{name}/libhbodbc.a}
%{_libdir}/%{name}/libhbct*.a
%{_libdir}/%{name}/liblang.a
%{_libdir}/%{name}/libmacro*.a
%{_libdir}/%{name}/libnulsys*.a
%{_libdir}/%{name}/libpp*.a
%{_libdir}/%{name}/librdd*.a
%{_libdir}/%{name}/librtl*.a
%{_libdir}/%{name}/libsamples.a
%{_libdir}/%{name}/libvm*.a
%{_libdir}/%{name}/libmain*.a
%{_libdir}/%{name}/libopt*.a

%files contrib
%defattr(644,root,root,755)
%{?with_nf:%{_libdir}/%{name}/libnf*.a}
%{?with_adsrdd:%{_libdir}/%{name}/librddads*.a}
%{?with_mysql:%{_libdir}/%{name}/libmysql*.a}
%{?with_pgsql:%{_libdir}/%{name}/libhbpg*.a}

%files lib
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%attr(755,root,root) %{_libdir}/*.so

%files pp
%defattr(644,root,root,755)
%doc utils/xbscript/xbscript.txt
%attr(755,root,root) %{_bindir}/xbscript
#%{_bindir}/pprun
#%{_bindir}/xprompt
