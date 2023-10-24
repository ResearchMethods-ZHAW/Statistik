- run `pandoc --extract-media ./images ReMe_Statistik-Skript_v.25.docx -o index.md`
- run `find . -name "*.emf" -exec inkscape -o {}.png {} \;`
- replance ".emf" with ".emf.png"
- replace "^$\n^\*\*(.+)\*\*" with "\n```{.r}\n$1\n```"
- replace "```\n\n```\{.r\}" with "\n"

