# Reset-contract and reactive diagrams

The self-contained `build_figures.py` uses Python and the pinned Matplotlib
dependency to draw four font-embedded vector PDFs directly, without TeX.
They depict the declared interface interval, initial/interior gap decomposition,
canonical microstep chain, and two-obligation viability example. They are
mathematical schematics rather than new experimental measurements.

Run `python figures/build_figures.py --outdir figures` from `artifact`.
The paper's compiler regenerates the same PDFs before its XeLaTeX build.
Scientific algorithms and the reproduction command remain standard-library
only; Matplotlib is an optional diagram-building dependency.
