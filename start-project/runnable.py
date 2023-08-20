from subprocess import run


class Runnable:
    def __init__(self, name, func, args, kwargs):
        self.name = name
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.func(*self.args, **self.kwargs)


class PnpmAddDevRunnable(Runnable):
    def __init__(self, name, dev=False):
        super().__init__(name, run_pnpm_add, [name, dev], {})

    def __str__(self):
        return f"ShellRunnable(command={self.args[0]})"

    def __repr__(self):
        return f"ShellRunnable(command={self.args[0]})"


class ShellRunnable(Runnable):
    def __init__(self, command):
        super().__init__("GENERIC", run_generic_shell, [command], {})

    def __str__(self):
        return f"ShellRunnable(command={self.args[0]})"

    def __repr__(self):
        return f"ShellRunnable(command={self.args[0]})"


def run_generic_shell(command):
    run(command, shell=True)


def run_pnpm_add_dev(args):
    run(f"pnpm add -D {args}", shell=True)


def run_pnpm_add(args):
    run(f"pnpm add {args}", shell=True)


def run_pnpm_create(args):
    run(f"pnpm create {args}", shell=True)


def run_pnpm_dlx(args):
    run(f"pnpm dlx {args}", shell=True)
