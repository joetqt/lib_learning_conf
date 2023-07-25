import _plotly_utils.basevalidators


class SizeValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self,
        plotly_name="size",
        parent_name="layout.xaxis.rangeselector.font",
        **kwargs,
    ):
        super(SizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
