# Clean reproduction record

This directory records a clean-copy replay in the same execution environment. It is not an independent external replication and it does not replace review of the mathematical proofs.

The standalone repository copy was created without Python caches or prior reproduced outputs. All 41 unit tests passed. The 22 scientific stages were then executed exactly once through the documented `--stage` interface into one fresh `reproduced/` directory. The resulting `summary.json` contains all 22 stages. `check_reproduction.py` matched 55 deterministic scientific files against the retained results with zero mismatches; CPU time, wall time, and peak RSS are deliberately excluded from semantic comparison because they are machine-dependent. The retained graph certificate was accepted by the command-line checker.

The clean scientific replay used one worker under the repository's 3 GiB address-space limit. Summed per-stage measurements were 73.446 CPU seconds and 73.479 wall seconds; the maximum per-stage peak RSS was 104,736 KiB. These are accounting measurements, not performance claims.

The paper was copied without `main.pdf` or LaTeX auxiliary files and rebuilt with `python3 build.py`. It produced exactly 50 pages and 40 bibliography entries. `paper-warning-scan.txt` is empty: no undefined citation/reference, overfull box, LaTeX error, fatal error, or rerun warning matched the scan. `paper-fonts.txt` records that all fonts are embedded. The source-only build used 7.23 user CPU seconds, 7.25 wall seconds, and 92,196 KiB maximum RSS.

`commands.txt` records the executed order. The repository also supports the ordinary one-command replay `python3 reproduce.py --output reproduced`; stage mode was used here so every bounded stage had a separate resource record.
