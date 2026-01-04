from typed import typed, Maybe, Str
from comp.mods.helper.comps import if_globals, if_aria, if_key
from comp.mods.err import HelperErr
from grid.mods.models import Column, Row, Grid

@typed
def if_col(col: Maybe(Column)=None) -> Str:
    try:
        if not col:
            return ""
        return (
            if_globals(col.col_globals)
          + if_aria(col.col_aria)
          + if_key(col.col_id,    "id")
          + if_key(col.col_class, "class")
          + if_key(col.col_style, "style")
        )
    except Exception as e:
        raise HelperErr(e)

@typed
def if_row(row: Maybe(Row)=None) -> Str:
    try:
        if not row:
            return ""
        return (
            if_globals(row.row_globals)
          + if_aria(row.row_aria)
          + if_key(row.row_id,    "id")
          + if_key(row.row_class, "class")
          + if_key(row.row_style, "style")
        )
    except Exception as e:
        raise HelperErr(e)

@typed
def if_grid(grid: Maybe(Grid)=None) -> Str:
    try:
        if not grid:
            return ""
        return (
            if_globals(grid.grid_globals)
          + if_aria(grid.grid_aria)
          + if_key(grid.grid_id,    "id")
          + if_key(grid.grid_class, "class")
          + if_key(grid.grid_style, "style")
        )
    except Exception as e:
        raise HelperErr(e)


def _render_inner(obj):
    try:
        if obj is None:
            return ""
        from grid.mods.comps  import col, row, grid
        if type(obj) is Column:     return col(obj)
        if type(obj) is Row:        return row(obj)
        if type(obj) is Grid:       return grid(obj)
        if isinstance(obj, str):    return obj
        return str(obj)
    except Exception as e:
        raise HelperErr(e)
