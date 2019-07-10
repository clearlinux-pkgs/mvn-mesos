#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-mesos
Version  : 1.4.0
Release  : 1
URL      : https://repo1.maven.org/maven2/org/apache/mesos/mesos/1.4.0/mesos-1.4.0.jar
Source0  : https://repo1.maven.org/maven2/org/apache/mesos/mesos/1.4.0/mesos-1.4.0.jar
Source1  : https://repo1.maven.org/maven2/org/apache/mesos/mesos/1.4.0/mesos-1.4.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-mesos-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-mesos package.
Group: Data

%description data
data components for the mvn-mesos package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/mesos/mesos/1.4.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/mesos/mesos/1.4.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/mesos/mesos/1.4.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/mesos/mesos/1.4.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/mesos/mesos/1.4.0/mesos-1.4.0.jar
/usr/share/java/.m2/repository/org/apache/mesos/mesos/1.4.0/mesos-1.4.0.pom
