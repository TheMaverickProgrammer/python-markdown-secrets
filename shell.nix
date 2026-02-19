let
	pkgs = import <nixpkgs> {};
	testDependencies = [
		pkgs.python3Packages.setuptools
		pkgs.mkdocs
		pkgs.python3Packages.pytest
	];
	mkdsecrets = pkgs.python3Packages.buildPythonPackage {
		pname = "python-markdown-secrets";
		version = "master";
		src = ./.;
		
		buildInputs = [
			pkgs.python3Packages.markdown
		];
		checkInputs = testDependencies;
		doCheck = false;
	};
in
	pkgs.mkShell {
		buildInputs = [
			mkdsecrets
		] ++ testDependencies;
	} 
