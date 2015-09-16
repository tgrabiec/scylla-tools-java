%define     origin_version  2.1.9

Name:           scylla-tools
Version:        0.00
Release:        1%{?dist}
Summary:        Scylla Tools
Group:          Applications/Dataases

License:        Apache
URL:            http://www.seastar-project.org/
Source0:        %{name}-%{version}.tar

BuildArch:      noarch
BuildRequires:  ant java-1.8.0-openjdk python
Requires:       java-1.8.0-openjdk python

%description


%prep
%setup -q


%build
env LANG=en_US.UTF-8 JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk ant jar

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}

cd pylib && python setup.py install --no-compile --root $RPM_BUILD_ROOT
cd -
install -d -m755 $RPM_BUILD_ROOT%{_sysconfdir}/cassandra
install -m644 conf/cassandra-env.sh $RPM_BUILD_ROOT%{_sysconfdir}/cassandra/
install -d -m755 $RPM_BUILD_ROOT%{_datadir}/cassandra/
install -m644 debian/cassandra.in.sh $RPM_BUILD_ROOT%{_datadir}/cassandra/
install -m755 bin/nodetool $RPM_BUILD_ROOT%{_bindir}
install -m755 bin/sstablekeys $RPM_BUILD_ROOT%{_bindir}
install -m755 bin/sstableloader $RPM_BUILD_ROOT%{_bindir}
install -m755 bin/cqlsh $RPM_BUILD_ROOT%{_bindir}
install -m755 bin/sstablescrub $RPM_BUILD_ROOT%{_bindir}
install -m755 bin/sstableupgrade $RPM_BUILD_ROOT%{_bindir}
install -m755 tools/bin/cassandra-stress $RPM_BUILD_ROOT%{_bindir}
install -m755 tools/bin/cassandra-stressd $RPM_BUILD_ROOT%{_bindir}
install -m755 tools/bin/json2sstable $RPM_BUILD_ROOT%{_bindir}
install -m755 tools/bin/sstable2json $RPM_BUILD_ROOT%{_bindir}
install -d -m755 $RPM_BUILD_ROOT%{_datadir}/cassandra/lib/
install -m644 lib/*.jar $RPM_BUILD_ROOT%{_datadir}/cassandra/lib/
install -m644 lib/*.zip $RPM_BUILD_ROOT%{_datadir}/cassandra/lib/
install -d -m755 $RPM_BUILD_ROOT%{_docdir}/cassandra/licenses/
install -m644 lib/licenses/* $RPM_BUILD_ROOT%{_docdir}/cassandra/licenses/

install -m644 build/apache-cassandra-%{origin_version}-SNAPSHOT.jar $RPM_BUILD_ROOT%{_datadir}/cassandra
install -m644 build/apache-cassandra-thrift-%{origin_version}-SNAPSHOT.jar $RPM_BUILD_ROOT%{_datadir}/cassandra
install -m644 build/tools/lib/stress.jar $RPM_BUILD_ROOT%{_datadir}/cassandra

cd $RPM_BUILD_ROOT
ln -s %{_datadir}/apache-cassandra-%{origin_version}-SNAPSHOT.jar $RPM_BUILD_ROOT%{_datadir}/cassandra/apache-cassandra.jar

%files
%{_sysconfdir}/cassandra/cassandra-env.sh
%{_datadir}/cassandra/cassandra.in.sh
%{_bindir}/nodetool
%{_bindir}/sstablekeys
%{_bindir}/sstableloader
%{_bindir}/cqlsh
%{_bindir}/sstablescrub
%{_bindir}/sstableupgrade
%{_bindir}/cassandra-stress
%{_bindir}/cassandra-stressd
%{_bindir}/json2sstable
%{_bindir}/sstable2json
%{_datadir}/cassandra/lib/*.jar
%{_datadir}/cassandra/lib/*.zip
%{_docdir}/cassandra/licenses
%{_datadir}/cassandra/apache-cassandra-%{origin_version}-SNAPSHOT.jar
%{_datadir}/cassandra/apache-cassandra.jar
%{_datadir}/cassandra/apache-cassandra-thrift-%{origin_version}-SNAPSHOT.jar
%{_datadir}/cassandra/stress.jar
%{_prefix}/lib/python2.7/site-packages/cassandra_pylib-0.0.0-py2.7.egg-info
%{_prefix}/lib/python2.7/site-packages/cqlshlib/__init__.py
%{_prefix}/lib/python2.7/site-packages/cqlshlib/__init__.pyc
%{_prefix}/lib/python2.7/site-packages/cqlshlib/__init__.pyo
%{_prefix}/lib/python2.7/site-packages/cqlshlib/cql3handling.py
%{_prefix}/lib/python2.7/site-packages/cqlshlib/cql3handling.pyc
%{_prefix}/lib/python2.7/site-packages/cqlshlib/cql3handling.pyo
%{_prefix}/lib/python2.7/site-packages/cqlshlib/cqlhandling.py
%{_prefix}/lib/python2.7/site-packages/cqlshlib/cqlhandling.pyc
%{_prefix}/lib/python2.7/site-packages/cqlshlib/cqlhandling.pyo
%{_prefix}/lib/python2.7/site-packages/cqlshlib/displaying.py
%{_prefix}/lib/python2.7/site-packages/cqlshlib/displaying.pyc
%{_prefix}/lib/python2.7/site-packages/cqlshlib/displaying.pyo
%{_prefix}/lib/python2.7/site-packages/cqlshlib/formatting.py
%{_prefix}/lib/python2.7/site-packages/cqlshlib/formatting.pyc
%{_prefix}/lib/python2.7/site-packages/cqlshlib/formatting.pyo
%{_prefix}/lib/python2.7/site-packages/cqlshlib/helptopics.py
%{_prefix}/lib/python2.7/site-packages/cqlshlib/helptopics.pyc
%{_prefix}/lib/python2.7/site-packages/cqlshlib/helptopics.pyo
%{_prefix}/lib/python2.7/site-packages/cqlshlib/pylexotron.py
%{_prefix}/lib/python2.7/site-packages/cqlshlib/pylexotron.pyc
%{_prefix}/lib/python2.7/site-packages/cqlshlib/pylexotron.pyo
%{_prefix}/lib/python2.7/site-packages/cqlshlib/saferscanner.py
%{_prefix}/lib/python2.7/site-packages/cqlshlib/saferscanner.pyc
%{_prefix}/lib/python2.7/site-packages/cqlshlib/saferscanner.pyo
%{_prefix}/lib/python2.7/site-packages/cqlshlib/sslhandling.py
%{_prefix}/lib/python2.7/site-packages/cqlshlib/sslhandling.pyc
%{_prefix}/lib/python2.7/site-packages/cqlshlib/sslhandling.pyo
%{_prefix}/lib/python2.7/site-packages/cqlshlib/tracing.py
%{_prefix}/lib/python2.7/site-packages/cqlshlib/tracing.pyc
%{_prefix}/lib/python2.7/site-packages/cqlshlib/tracing.pyo
%{_prefix}/lib/python2.7/site-packages/cqlshlib/util.py
%{_prefix}/lib/python2.7/site-packages/cqlshlib/util.pyc
%{_prefix}/lib/python2.7/site-packages/cqlshlib/util.pyo
%{_prefix}/lib/python2.7/site-packages/cqlshlib/wcwidth.py
%{_prefix}/lib/python2.7/site-packages/cqlshlib/wcwidth.pyc
%{_prefix}/lib/python2.7/site-packages/cqlshlib/wcwidth.pyo

%changelog
* Fri Aug  7 2015 Takuya ASADA Takuya ASADA <syuu@cloudius-systems.com>
- inital version of scylla-tools.spec
