#
# Conditional build:
#%bcond_with	tests		# build with tests
#%bcond_without	tests		# build without tests
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
#Source1:	-
# Source1-md5:	-
#Patch0:		%{name}-what.patch
URL:		http://www.xharbour.org
#BuildRequires:	-
#PreReq:		-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
#Requires:	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{dname} is a CA-Clipper compatible compiler for multiple platforms. This
package includes a compiler, pre-processor, header files, virtual machine
and documentation.

See README.RPM in the documentation directory for information specific to
this RPM distribution.

%description -l pl
%{dname} to kompatybilny z jЙzykiem CA-Clipper kompilator rozwijany na
wielu rС©nych platformach. Ten pakiet zawiera kompilator, preprocesor,
zbiory nagЁСwkowe, wirtualn╠ maszynЙ oraz dokumentacjЙ.

%description -l pt_BR
%{dname} ~B um compilador Clipper compativel para multiplas plataformas.
Esse pacote contem um compilador, um pr~B-processador, arquivos de cabe~Galho
uma maquina virtual e documenta~Gфo.

%description -l ru
%{dname} - многоплатформенный компилятор, совместимый с языком CA-Clipper.
Этот пакет содержит компилятор, препроцессор, файлы заголовков, виртуальную
машину и документацию.

#%package subpackage
#Summary:	-
#Summary(pl):	-
#Group:		-
######		Unknown group!

#%description subpackage

#%description subpackage -l pl

%prep
%setup -q 

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}


######################################################################
# Conditional build:
# --with static      - link all binaries with static libs
# --with adsrdd      - build ads RDD
# --with mysql       - build mysql lib
# --with pgsql       - build pgsql lib
# --with odbc        - build build odbc lib
# --with hrbsh       - build /etc/profile.d/harb.sh (not necessary)
# --without nf       - do not build nanforum lib
# --without x11      - do not build GTXVT and GTXWC
# --without gpm      - build GTSLN and GTCRS without GPM support
# --without gtsln    - do not build GTSLN
######################################################################

%if "%{platform}" == ""
%define platform %([ -f /etc/pld-release ] && cat /etc/pld-release|sed -e '/1/ !d' -e 's/[^0-9]//g' -e 's/^/pld/')
%endif

%define prefix   /usr
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
%define hb_bdir  export HB_BIN_INSTALL=%{prefix}/bin
%define hb_idir  export HB_INC_INSTALL=%{prefix}/include/%{name}
%define hb_ldir  export HB_LIB_INSTALL=%{prefix}/lib/%{name}
%define hb_opt   export HB_GTALLEG=%{?_with_allegro:yes}
%define hb_cmrc  export HB_COMMERCE=no
%define hb_ctrb  %{!?_without_nf:libnf} %{?_with_adsrdd:rdd_ads} %{?_with_mysql:mysql} %{?_with_pgsql:pgsql}
%define hb_env   %{hb_arch} ; %{hb_cc} ; %{hb_cflag} ; %{hb_lflag} ; %{hb_mt} ; %{hb_gt} ; %{hb_gpm} ; %{hb_sln} ; %{hb_x11} ; %{hb_mgt} ; %{hb_bdir} ; %{hb_idir} ; %{hb_ldir} ; %{hb_opt} ; %{hb_cmrc}

%define hb_host  www.xharbour.org
%define readme   README.RPM

%{hb_env}

make -r

# build contrib libraries
for l in %{hb_ctrb}
do
    (cd "contrib/$l"
     make -r)
done

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

%attr(755,root,root) %{_bindir}/*

%{_datadir}/%{name}

# initscript and it's config
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

#%files subpackage
#%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
