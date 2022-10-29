# ScreenScraping using Python metaclass
## ... just because you can.

Extracted from [Daniel Pope - Writing Domain Specific Languages with Python - YouTube](https://www.youtube.com/watch?v=wQAPRfEOb10&t=539s&ab_channel=EuroPythonConference)
by [lordmauve (Daniel Pope)](https://github.com/lordmauve)

# pyright language server
Within nvim try `:LspInfo` to get general info (when in a Python buffer)

Recommended config in `pyrightconfig.json` but not actually needed.

    {
        "extraPaths": ["."],
        "executionEnvironments": [
            {"root": "."}
        ]
    }

and yet just an empty file `pyrightconfig.json` was good enough to fix the issue
    Import could not be resolved

The file effectively marks the project root.

