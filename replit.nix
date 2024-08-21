{pkgs}: {
  deps = [
    pkgs.dotnetCorePackages.sdk_7_0_3xx
    pkgs.percona-server
  ];
}
