|Treeview||
|--|--|
| `class_` | You may provide a widget class name when you create this widget. This name may be used to customize the widget's appearance; see [Section 27, “Standardizing appearance”](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/option-database.html "27. Standardizing appearance and the option database"). Once the widget is created, the widget class name cannot be changed. |
| `columns` |A sequence of column identifier strings. These strings are used internally to identify the columns within the widget. The icon column, whose identifier is always `'#0'`, contains the collapse/expand icons and is always the first column.<br> The columns you specify with the `columns` argument are in addition to the icon column.<br>For example, if you specified `columns=('Name', 'Size')`, three columns would appear in the widget: first the icon column, then two more columns whose internal identifiers are `'Name'` and `'Size'`. |
| `cursor` | Use this option to specify the appearance of the mouse cursor when it is over the widget; see [Section 5.8, “Cursors”](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/cursors.html "5.8. Cursors"). The default value (an empty string) specifies that the cursor is inherited from the parent widget. |
| `displaycolumns` | Selects which columns are actually displayed and determines the order of their presentation. Values may be: <br> 1. `#all` to select all columns and display them in the order defined by the `columns` argument.<br> 2. A list of column numbers (integer positions, counting from 0) or column identifiers from the `columns` argument. <br>    For example, suppose you specify `columns=('Name', 'Size', 'Date')`. This means each call to the `.insert()` method will require an argument ``values=(_`name`_, _`size`_, _`date`_)`` to supply the values that will be displayed. Let's call this sequence the _logical column sequence_. <br>    Further suppose that in the constructor you specify `columns=(2,0)`. The _physical column sequence_, the columns that will actually appear in the widget, will be three: the icon column will be first, followed by the date column (index 2 in the logical column sequence), followed by the name column (logical column index 0). The size column will not appear. <br>    You could get the same effect by specifying column identifiers instead of logical column positions: `columns=('Date', 'Name')`. |
| `height` | The desired height of the widget, in rows. |
| `padding` | Use this argument to place extra space around the contents inside the widget. You may provide either a single [dimension](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/dimensions.html "5.1. Dimensions") or a sequence of up to four dimensions, interpreted according to this table: <br> 

| Values given | Left | Top | Right | Bottom |
| :-- | :-: | :-: | :-: | :-: |
| _a_ | _a_ | _a_ | _a_ | _a_ |
| _a b_ | _a_ | _b_ | _a_ | _b_ |
| _a b c_ | _a_ | _c_ | _b_ | _c_ |
| _a b c d_ | _a_ | _b_ | _c_ | _d_ |

|


|Treeview||
|--|--|
| `selectmode` | This option controls what the user is allowed to select with the mouse. Values can be:

|||
|--|--|
| `selectmode='browse'` | The user may select only one item at a time. |
| `selectmode='extended'` | The user may select multiple items at once. |
| `selectmode='none'` | The user cannot select items with the mouse. |


|Treeview||
|--|--|
| `show` | To suppress the labels at the top of each column, specify `show='tree'`. The default is to show the column labels. |
| `style` | Use this option to specify a custom widget style name; see [Section 47, “Customizing and creating ttk themes and styles”](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-themes.html "47. Customizing and creating ttk themes and styles"). |
| `takefocus` | Use this option to specify whether a widget is visited during focus traversal; see [Section 53, “Focus: routing keyboard input”](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/focus.html "53. Focus: routing keyboard input"). Specify `takefocus=True` if you want the visit to accept focus; specify `takefocus=False` if the widget is not to accept focus. The default value is an empty string; by default, ttk`.Treeview` widgets do get focus. |



|`insert`(_parent_, _index_, _iid=None_, _**kw_)[]|[link](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert "Permalink to this definition")<br>Creates a new item and returns the item identifier of the newly created item.|
|-|-|
| _parent_ | item ID of parent item, or empty string to create a new top-level item. |
| _index_ | an integer, or the value “end”, specifying where in the list of parent’s children to insert the new item. <br> If _index_ <= 0 , new node is inserted at the beginning; <br> if _index_ >= current number of children, it is inserted at the end. | 
| _iid_ | If is specified, it is used as the item identifier; <br> _iid_must not already exist in the tree. Otherwise, a new unique identifier is generated. 

