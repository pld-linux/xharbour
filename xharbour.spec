#
# Conditional build:
# --with static      - link all binaries with static libs
# --with adsrdd      - build ads RDD
# --with mysql       - build mysql lib
# --with pgsql       - build pgsql lib
# --with odbc        - build build odbc lib
# --with hrbsh       - build /etc/profile.d/harb.sh (not necessary)
# --without x11      - do not build GTXVT and GTXWC
# --without gpm      - build GTSLN and GTCRS without GPM support
# --without gtsln    - do not build GTSLN
# --without nf       - do not build nanforum lib doesn't work now.
######################################################################
######################################################################
#
# TODO:
# nf
# pprun
#
Summary:	Backwards compatible Clipper Language compiler and preprocessor.
Summary(pl):	Zgodny wstecz kompilator clippera oraz preprocesor
Name:		xharbour
Version:	0.99.3
Release:	0.1
Epoch:		0
License:	GPL v2
#Vendor:		-
Group:		Development/Languages
#Icon:		-
Source0:	http://files.xharbour.org/source/%{name}-%{version}.src.tar.gz
# Source0-md5:	7e660044656df06d98589da25285fc20
Source1:	http://files.xharbour.org/source/%{name}-%{version}.src.contrib.tar.gz
URL:		http://www.xharbour.org
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{dname} is a CA-Clipper compatible compiler for multiple platforms.
This package includes a compiler, pre-processor, header files, virtual
machine and documentation.

See README.RPM in the documentation directory for information specific
to this RPM distribution.

%description -l pl
%{dname} to kompatybilny z jЙzykiem CA-Clipper kompilator rozwijany na
wielu rС©nych platformach. Ten pakiet zawiera kompilator, preprocesor,
zbiory nagЁСwkowe, wirtualn╠ maszynЙ oraz dokumentacjЙ.

%description -l pt_BR
%{dname} ~B um compilador Clipper compativel para multiplas
plataformas. Esse pacote contem um compilador, um pr~B-processador,
arquivos de cabe~Galho uma maquina virtual e documenta~Gфo.

%description -l ru
%{dname} - многоплатформенный компилятор, совместимый с языком
CA-Clipper. Этот пакет содержит компилятор, препроцессор, файлы
заголовков, виртуальную машину и документацию.


%package lib
Summary:	Shared runtime libaries for %{dname} compiler
Summary(pl):	Dzielone bilioteki dla kompilatora %{dname}
Summary(ru):	Совместно используемые библиотеки для компилятора %{dname}
Group:		Development/Languages
Provides:	lib%{name}.so lib%{name}mt.so

%description lib
%{dname} is a Clipper compatible compiler. This package provides
%{dname} runtime shared libraries for programs linked dynamically.

%description lib -l pl
%{dname} to kompatybilny z jЙzykiem CA-Clipper kompilator. Ten pakiet
udostЙpnia dzielone bilioteki kompilatora %{dname} dla programСw
konsolidowanych dynamicznie.

%description lib -l pt_BR
%{dname} ~B um compilador compativel com o Clipper. Esse pacote
%{dname} provem as bibliotecas compartilhadas para programas linkados
dinamicamente.

%description lib -l ru
%{dname} - компилятор, совместимый с языком CA-Clipper. Этот пакет
содержит совместно используемые библиотеки %{dname}, необходимые для
работы динамически скомпонованных программ.


%package static
Summary:	Static runtime libaries for %{dname} compiler
Summary(pl):	Statyczne bilioteki dla kompilatora %{dname}
Summary(ru):	Статические библиотеки для компилятора %{dname}
Group:		Development/Languages
Requires:	%{name} = %{version}

%description static
%{dname} is a Clipper compatible compiler. This package provides
%{dname} static runtime libraries for static program linking.

%description static -l pl
%{dname} to kompatybilny z jЙzykiem CA-Clipper kompilator. Ten pakiet
udostЙpnia statyczne bilioteki dla kompilatora %{dname} niezbЙdne do
statycznej konsolidacji programСw.

%description static -l pt_BR
%{dname} ~B um compilador compativel com o clippe. Esse pacote
%{dname} provem as bibliotecas de run time staticas para linkagem dos
os programas

%description static -l ru
%{dname} - компилятор, совместимый с языком CA-Clipper. Этот пакет
содержит статические библиотеки компилятора %{dname}, необходимые для
статической компоновки программ.



%package contrib
Summary:	Contrib runtime libaries for %{dname} compiler
Summary(pl):	Bilioteki z drzewa contrib dla kompilatora %{dname}
Summary(pt_BR):	Libs contrib para %{dname}
Summary(ru):	Библиотеки из дерева contrib для компилятора %{dname}
Group:		Development/Languages
Requires:	%{name} = %{version}

%description contrib
%{dname} is a Clipper compatible compiler. This package provides
%{dname} contrib libraries for program linking.

%description contrib -l pl
%{dname} to kompatybilny z jЙzykiem CA-Clipper kompilator. Ten pakiet
udostЙpnia statyczne bilioteki z drzewa contrib dla kompilatora
%{dname}.

%description contrib -l pt_BR
%{dname} ~B um compilador compativel com o clippe. Esse pacote
%{dname} provem as bibliotecas contrib para linkagem dos programas.

%description contrib -l ru
%{dname} - компилятор, совместимый с языком CA-Clipper. Этот пакет
содержит статические библиотеки %{dname} из дерева contrib.


%package pp
Summary:	Clipper/Harbour/xBase compatible Pre-Processor, DOT prompt and interpreter
Summary(pl):	Kompatybilny z Clipper/Harbour/xBase Preprocesor i interpreter
Summary(ru):	Совместимый с Clipper/Harbour/xBase препроцессор и интерпретатор
License:	GPL
Group:		Development/Languages
Requires:	%{name} = %{version}

%description pp
%{dname} is a Clipper compatible compiler. This package provides
%{dname} PP. It has 3 personalities which are tied tightly together.
1. What is supposed to be 100% Clipper compatible Pre-Processor (with
some extensions). 2. DOT prompt, which suppose to allow most of
Clipper syntax. 3. Finally, PP is a limited Clipper/Harbour/xBase
Interpreter. Subject to those same few limitations it can execute most
of Harbour syntax. You can write your own xBase scripts by adding to
your .prg files #!/usr/bin/pprun

%description pp -l pl
%{dname} to kompatybilny z jЙzykiem CA-Clipper kompilator. Ten pakiet
udostЙpnia %{dname} PP, ktСry daje trzy narzЙdzia w jednym. 1. W 100%
kompatybilny z Clipperem preprocesor (z pewnymi rozeszerzeniami) 2.
╕rodowisko DOT, w ktСrym mo©na u©ywaФ wiЙkszo╤ci skЁadni Clippera 3.
PP to tak©e nieco ograniczony interpreter Clippera. Z uwzglЙdnieniem
wspomnianych kilku ograniczeЯ potrafi on uruchomiФ wiЙkszo╤Ф skЁadni
Harbour. Mo©esz napisaФ swСj wЁasny skrypt xBase dodaj╠c do pliku .prg
#!/usr/bin/pprun

%description pp -l pt_BR
%{dname} ~B um compilador Clipper compativel. Esse pacote provem o
%{dname} PP. Ele tem 3 caracteristicas dependentes uma da outra. 1.
Que e supostamente ser um Pre-Processor 100% compativel com o Clipper
(com algumas extenssДes). 2. DOT prompt, que supostamente permite a
maioria das syntaxes do Clipper. 3. Finalmente, PP ~B um limitado
Interpretador Clipper/Harbour/xBase . Sujeito com algumas limita~GДes
que pode executar a maioria da syntaxe do Harbour. Voce pode escrever
seus proprios scritps em .prg ao adicionar as seus arquivos .prg
#!/usr/bin/pprun

%description pp -l ru
%{dname} - компилятор, совместимый с языком CA-Clipper. Этот пакет
содержит препроцессор %{dname}, который состоит из трех тесно
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
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}


######################################################################

%if "%{platform}" == ""
%define platform %([ -f %{_sysconfdir}/pld-release ] && cat %{_sysconfdir}/pld-release|sed -e '/1/ !d' -e 's/[^0-9]//g' -e 's/^/pld/')
%endif

%define prefix %{_prefix}
%define hb_pref  xhb
%define hb_arch  export HB_ARCHITECTURE=linux
%define hb_cc    export HB_COMPILER=gcc
%define hb_cflag export C_USR="-DHB_FM_STATISTICS_OFF -O3"
%define hb_lflag export L_USR=%{?_with_static:-static}
%define hb_mt    export HB_MT=MT
%define hb_mgt   export HB_MULTI_GT=yes
%define hb_gt    export HB_GT_LIB=gtcrs
%define hb_gpm   export HB_GPM_MOUSE=%{!?_without_gpm:yes}
%define hb_sln   export HB_WITHOUT_GTSLN=%{?_without_gtsln:yes}
%define hb_x11   export HB_WITHOUT_X11=%{?_without_x11:yes}
%define hb_bdir  export HB_BIN_INSTALL=%{_bindir}
%define hb_idir  export HB_INC_INSTALL=%{_includedir}/%{name}
%define hb_ldir  export HB_LIB_INSTALL=%{_prefix}/lib/%{name}
%define hb_opt   export HB_GTALLEG=%{?_with_allegro:yes}
%define hb_cmrc  export HB_COMMERCE=no
%define hb_ctrb  %{!?_without_nf:libnf} %{?_with_adsrdd:rdd_ads} %{?_with_mysql:mysql} %{?_with_pgsql:pgsql}
%define hb_env   %{hb_arch} ; %{hb_cc} ; %{hb_cflag} ; %{hb_lflag} ; %{hb_mt} ; %{hb_gt} ; %{hb_gpm} ; %{hb_sln} ; %{hb_x11} ; %{hb_mgt} ; %{hb_bdir} ; %{hb_idir} ; %{hb_ldir} ; %{hb_opt} ; %{hb_cmrc}

%define hb_host  www.xharbour.org
%define readme   README.RPM

%{hb_env}

%{__make}

# build contrib libraries
for l in %{hb_ctrb}
do
    (cd "contrib/$l"
    %{__make} )
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
    (cd "contrib/$l"
    %{__make} install )
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
#%verify(not md5 mtime) %config /etc/harbour.cfg
#%verify(not md5 mtime) %config /etc/harbour/hb-charmap.def
%{?_with_hrbsh:/etc/profile.d/harb.sh}

%attr(755,root,root)
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
%dir %{_prefix}/lib/%{name}
%{_prefix}/lib/%{name}/libcodepage.a
%{_prefix}/lib/%{name}/libcommon.a
%{_prefix}/lib/%{name}/libdb*.a
%{_prefix}/lib/%{name}/libdebug.a
%{_prefix}/lib/%{name}/libfm*.a
%{_prefix}/lib/%{name}/libgt*.a
%{_prefix}/lib/%{name}/libhbtip*.a
%{?_with_odbc: %{_prefix}/lib/%{name}/libhbodbc.a}
%{_prefix}/lib/%{name}/libhbct*.a
%{_prefix}/lib/%{name}/liblang.a
%{_prefix}/lib/%{name}/libmacro*.a
%{_prefix}/lib/%{name}/libnulsys*.a
%{_prefix}/lib/%{name}/libpp*.a
%{_prefix}/lib/%{name}/librdd*.a
%{_prefix}/lib/%{name}/librtl*.a
%{_prefix}/lib/%{name}/libsamples.a
%{_prefix}/lib/%{name}/libvm*.a
%{_prefix}/lib/%{name}/libmain*.a
%{_prefix}/lib/%{name}/libopt*.a

%files contrib
%defattr(644,root,root,755)
%dir %{_prefix}/lib/%{name}
%{!?_without_nf: %{_prefix}/lib/%{name}/libnf*.a}
%{?_with_adsrdd: %{_prefix}/lib/%{name}/librddads*.a}
%{?_with_mysql: %{_prefix}/lib/%{name}/libmysql*.a}
%{?_with_pgsql: %{_prefix}/lib/%{name}/libhbpg*.a}

%files lib
%defattr(644,root,root,755)
%dir %{_prefix}/lib/%{name}
%{_prefix}/lib/%{name}/*.so
%{_prefix}/lib/*.so

%files pp
%defattr(644,root,root,755)
%doc utils/xbscript/xbscript.txt
%attr(755,root,root) %{_bindir}/xbscript
#%{prefix}/bin/pprun
#%{prefix}/bin/xprompt
