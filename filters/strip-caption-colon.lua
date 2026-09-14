-- Strips the leading ": " from table captions produced by the list-table
-- ": Caption" syntax, which would otherwise render as "Tabelle N: : Caption"
-- in KOMA-script PDF output.
function Table(tbl)
  if tbl.caption and tbl.caption.long and #tbl.caption.long > 0 then
    local block = tbl.caption.long[1]
    if (block.t == "Plain" or block.t == "Para") and #block.content >= 2 then
      if block.content[1].t == "Str" and block.content[1].text == ":" and
         block.content[2].t == "Space" then
        table.remove(block.content, 1)
        table.remove(block.content, 1)
      end
    end
  end
  return tbl
end
