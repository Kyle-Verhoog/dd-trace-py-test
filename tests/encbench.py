import pytest
import ddtrace


class Q(object):

    def put(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        pass


@pytest.mark.benchmark(group="create_spans", min_time=0.005)
def test_tracer_trace(benchmark):
    ddtrace.tracer.writer._trace_queue = Q()

    @benchmark
    def f():
        for i in range(10):
            ddtrace.tracer.trace("operation").finish()


@pytest.mark.benchmark(group="create_spans", min_time=0.005)
def test_tracer_trace2(benchmark):
    ddtrace.tracer.writer._trace_queue = Q()

    @benchmark
    def f():
        for i in range(2):
            with ddtrace.tracer.trace("wtf"):
                for _ in range(10):
                    ddtrace.tracer.trace("operation").finish()
