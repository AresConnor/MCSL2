def installProfilerCallback():
    import sys
    import traceback
    from typing import Any
    from types import FrameType
    def _(frame: FrameType, event: str, arg: Any):
        try:
            code = frame.f_code
            filename = code.co_filename
            lineno = code.co_firstlineno
            fn_name = code.co_name
            print(f"{event:<10} | {filename}:{lineno} => {fn_name}({arg})")
        except:
            traceback.print_exc()

    sys.setprofile(_)