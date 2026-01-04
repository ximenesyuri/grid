from typed import Maybe
from comp import comp, Jinja, Inner
from comp.mods.err import CompErr
from grid.mods.models import Column, Row, Grid
from grid.mods.helper import if_col, if_row, if_grid, _render_inner

@comp
def col(col: Maybe(Column)=None, inner: Inner="") -> Jinja:
    try:
        if col is None:
            col = Column()
        existing = col.col_class or ""
        if "col" not in existing.split():
            col.col_class = (existing + " col").strip()
        if col.col_inner:
            rendered_inner = _render_inner(col.col_inner)
        elif inner:
            rendered_inner = _render_inner(inner)
        else:
            rendered_inner = ""
        return f"""jinja
<div{ if_col(col) }>{ rendered_inner }</div>
"""
    except Exception as e:
        raise CompErr(e)

@comp
def col_1(col: Maybe(Column)=None, inner: Inner="") -> Jinja:
    try:
        if col is None:
            col = Column()
        existing = col.col_class or ""
        if "col-1" not in existing.split():
            col.col_class = (existing + " col-1").strip()
        if col.col_inner:
            rendered_inner = _render_inner(col.col_inner)
        elif inner:
            rendered_inner = _render_inner(inner)
        else:
            rendered_inner = ""
        return f"""jinja
<div{ if_col(col) }>{ rendered_inner }</div>
"""
    except Exception as e:
        raise CompErr(e)

@comp
def col_2(col: Maybe(Column)=None, inner: Inner="") -> Jinja:
    try:
        if col is None:
            col = Column()
        existing = col.col_class or ""
        if "col-2" not in existing.split():
            col.col_class = (existing + " col-2").strip()
        if col.col_inner:
            rendered_inner = _render_inner(col.col_inner)
        elif inner:
            rendered_inner = _render_inner(inner)
        else:
            rendered_inner = ""
        return f"""jinja
<div{ if_col(col) }>{ rendered_inner }</div>
"""
    except Exception as e:
        raise CompErr(e)

@comp
def col_3(col: Maybe(Column)=None, inner: Inner="") -> Jinja:
    try:
        if col is None:
            col = Column()
        existing = col.col_class or ""
        if "col-3" not in existing.split():
            col.col_class = (existing + " col-3").strip()
        if col.col_inner:
            rendered_inner = _render_inner(col.col_inner)
        elif inner:
            rendered_inner = _render_inner(inner)
        else:
            rendered_inner = ""
        return f"""jinja
<div{ if_col(col) }>{ rendered_inner }</div>
"""
    except Exception as e:
        raise CompErr(e)

@comp
def col_4(col: Maybe(Column)=None, inner: Inner="") -> Jinja:
    try:
        if col is None:
            col = Column()
        existing = col.col_class or ""
        if "col-4" not in existing.split():
            col.col_class = (existing + " col-4").strip()
        if col.col_inner:
            rendered_inner = _render_inner(col.col_inner)
        elif inner:
            rendered_inner = _render_inner(inner)
        else:
            rendered_inner = ""
        return f"""jinja
<div{ if_col(col) }>{ rendered_inner }</div>
"""
    except Exception as e:
        raise CompErr(e)

@comp
def col_5(col: Maybe(Column)=None, inner: Inner="") -> Jinja:
    try:
        if col is None:
            col = Column()
        existing = col.col_class or ""
        if "col-5" not in existing.split():
            col.col_class = (existing + " col-5").strip()
        if col.col_inner:
            rendered_inner = _render_inner(col.col_inner)
        elif inner:
            rendered_inner = _render_inner(inner)
        else:
            rendered_inner = ""
        return f"""jinja
<div{ if_col(col) }>{ rendered_inner }</div>
"""
    except Exception as e:
        raise CompErr(e)

@comp
def row(row: Maybe(Row)=None, __context__={"col": col}) -> Jinja:
    try:
        if row is None:
            row = Row()
        existing = row.row_class or ""
        if "row" not in existing.split():
            row.row_class = (existing + " row").strip()
        return f"""jinja
<div{ if_row(row) }>[% if row.row_cols is defined %][% for c in row.row_cols %]
    [[ col(col=c) ]][% endfor %]
</div>[% else %]</div>[% endif %]
"""
    except Exception as e:
        raise CompErr(e)

@comp
def grid(grid: Maybe(Grid)=None, __context__={"row": row}) -> Jinja:
    try:
        if grid is None:
            grid = Grid()
        return f"""jinja
<div{ if_grid(grid) }>[% if grid.grid_rows is defined %][% for r in grid.grid_rows %]
    [[ row(row=r) ]][% endfor %]
</div>[% else %]</div>[% endif %]
"""
    except Exception as e:
        raise CompErr(e)
