|grid 參數||
|-------------|---------------|
| `row` | The row number into which you want to insert the widget, counting from 0. The default is the next higher-numbered unoccupied row. |
| `rowspan` | Normally a widget occupies only one cell in the grid. You can grab multiple adjacent cells of a column, however, by setting the `rowspan` option to the number of cells to grab. This option can be used in combination with the `columnspan` option to grab a block of cells. For example, ``_`w`_.grid(row=3, column=2, rowspan=4, columnspan=5)`` would place widget ``_`w`_`` in an area formed by merging 20 cells, with row numbers 3–6 and column numbers 2–6. |
| `column` | column position (from 0) |
| `columnspan` | For example, w.grid(row=0, column=2, columnspan=3) would place widget w in a cell that spans columns 2, 3, and 4 of row 0. |
| `ipadx` | Internal x padding. This dimension is added inside the widget inside its left and right sides. |
| `ipady` | Internal y padding. This dimension is added inside the widget inside its top and bottom borders. |
| `padx` | External x padding. This dimension is added to the left and right outside the widget. |
| `pady` | External y padding. This dimension is added above and below the widget. |
| `sticky` | sticky='w'+'e'+'n'+'s' |


|row & column configure||
|-------------|---------------|
| `minsize` | The column or row's minimum size in pixels. If there is nothing in the given column or row, it will not appear, even if you use this option. |
| `pad` | A number of pixels that will be added to the given column or row, over and above the largest cell in the column or row. |
| `weight` | stretchable, gives the relative weight of this column or row. For example, if a widget `w` contains a grid layout, these lines will distribute three-fourths of the extra space to the first column and one-fourth to the second column:<br>`w.columnconfigure(0, weight=3)`<br>`w.columnconfigure(1, weight=1)`<br>If this option is not used, the column or row will not stretch. |