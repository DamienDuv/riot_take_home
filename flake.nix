{
  description = "Dev shell for Riot's challenge (uv + Python)";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs, ... }:
  let
    systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
    forAllSystems = nixpkgs.lib.genAttrs systems;
  in {
    devShells = forAllSystems (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in {
        default = pkgs.mkShell {
          packages = [ 
            pkgs.python312 
            pkgs.uv 
            pkgs.fastapi-cli
            ];
          shellHook = ''
            export UV_PYTHON="$(command -v python3.12)"
            export UV_NO_MANAGED_PYTHON=1
            export UV_PYTHON_DOWNLOADS=0
            echo "Dev shell ready on ${system}: $(python3 --version); uv $(uv --version)"
          '';
        };
      });
  };
}
