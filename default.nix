with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "env";

  # Mandatory boilerplate for buildable env
  env = buildEnv { name = name; paths = buildInputs; };
  builder = builtins.toFile "builder.sh" ''
    source $stdenv/setup; ln -s $env $out
  '';

  # Customizable development requirements
  buildInputs = [
    # Add packages from nix-env -qaP | grep -i needle queries
    python3
    ngrok-1
    python3Packages.tensorflow
    libffi
    openmpi
  ];

  # Customizable development shell setup with at last SSL certs set
  shellHook = ''
    export NIX_CFLAGS_COMPILE="$NIX_CFLAGS_COMPILE -isystem ${python3}/include/python3.6"
    source venv/bin/activate
  '';
}
