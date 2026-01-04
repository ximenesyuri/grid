from utils.general import lazy

__imports__ = {
    "col":           "grid.mods.comps",
    "col_1":         "grid.mods.comps",
    "col_2":         "grid.mods.comps",
    "col_3":         "grid.mods.comps",
    "col_4":         "grid.mods.comps",
    "col_5":         "grid.mods.comps",
    "row":           "grid.mods.comps",
    "grid":          "grid.mods.comps",
    "Col":           "grid.mods.models",
    "Row":           "grid.mods.models",
    "Grid":          "grid.mods.models",
    "GridEntity":    "grid.mods.models",
    "GridFactory":   "grid.mods.models",
    "build_col":     "grid.mods.builds",
    "build_row":     "grid.mods.builds",
    "build_grid":    "grid.mods.builds",
    "build_comp":    "grid.mods.builds",
    "build_factory": "grid.mods.builds",
}


if lazy(__imports__):
    from grid.mods.comps import (
        col, col_1, col_2, col_3, col_4, col_5, row, grid
    )
    from grid.mods.models import (
        Col, Row, Grid, GridEntity, GridFactory
    )
    from grid.mods.builds import (
        build_col, build_row, build_grid, build_comp, build_factory
    )
