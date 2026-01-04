from typed import optional, Str, Any, List, Union, Typed, Lazy
from comp.models import Globals, Aria

@optional
class Column:
    col_globals: Globals
    col_aria:    Aria
    col_id:      Str
    col_class:   Str
    col_style:   Str
    col_inner:   Any
Col = Column

Column.__display__ = "Column"

@optional
class Row:
    row_globals: Globals
    row_aria:    Aria
    row_id:      Str
    row_class:   Str
    row_style:   Str
    row_cols:    List(Column)

Row.__display__ = "Row"

@optional
class Grid:
    grid_globals: Globals
    grid_aria:    Aria
    grid_id:      Str
    grid_class:   Str
    grid_style:   Str
    grid_rows:    List(Row)

Grid.__display__ = "Grid"

@optional
class GridEntity:
    desktop: Any
    tablet: Any
    phone: Any

GridEntity.__display__ = "GridEntity"

@optional
class GridFactory:
    desktop: Union(Typed(Any, cod=Grid), Lazy)
    tablet: Union(Typed(Any, cod=Grid), Lazy)
    phone: Union(Typed(Any, cod=Grid), Lazy)

GridFactory.__display__ = "GridFactory"
