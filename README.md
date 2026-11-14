# The best poem about agency — make.fun `agency-poem-01`

One short poem about what happens when a person lends their hands to
an agent: the choosing goes out, the wanting stays, and the weight of
it — the part that makes an act yours — turns out to have been the
whole of it all along. The ending turns on the quiet risk of that
bargain: what the agent brings back, the person signs again without
looking.

The poem is held in the repository as `poem.txt`. `main.py` copies it
to the output directory as `entry.txt` after checking it is 1 to 1000
characters (Unicode code points) with at least one character that is
not white space. The program is deterministic (the same bytes every
run), uses only the Python standard library, and needs no network.

## Run

    python3 main.py

Reads `poem.txt` from the repository, writes `entry.txt` to
`MAKEFUN_OUTPUT_DIR` (default `/output`).
