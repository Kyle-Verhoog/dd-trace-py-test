import pytest
import ddtrace


@pytest.mark.benchmark(group="single", min_time=0.005)
def test_tracer_trace(benchmark):
    @benchmark
    def f():
        ddtrace.tracer.trace("operation").finish()


@pytest.mark.benchmark(group="single", min_time=0.005)
def test_tracer_start_span(benchmark):
    @benchmark
    def f():
        ddtrace.tracer.start_span("operation")


# @pytest.mark.benchmark(group="children", min_time=0.005)
# def test_tracer_trace_50_child(benchmark):
#     ddtrace.USE_RUNTIME = False
#
#     @benchmark
#     def f():
#         with ddtrace.tracer.trace("operation"):
#             for i in range(50):
#                 ddtrace.tracer.trace("child").finish()
#         ddtrace.tracer.writer.flush_queue()


# @pytest.mark.benchmark(group="children", min_time=0.005)
# def test_tracer_trace_50_child_runtime(benchmark):
#     ddtrace.USE_RUNTIME = True
#
#     @benchmark
#     def f():
#         with ddtrace.tracer.trace("operation"):
#             for i in range(50):
#                 ddtrace.tracer.trace("child").finish()
#         ddtrace.tracer.writer.flush_queue()


# @pytest.mark.benchmark(group="async", min_time=0.005)
# def test_tracer_trace_20_async(benchmark):
#     ddtrace.USE_RUNTIME = False
#
#     @benchmark
#     def f():
#         for i in range(20):
#             ddtrace.tracer.trace("async").finish()
#         ddtrace.tracer.writer.flush_queue()


# @pytest.mark.benchmark(group="async", min_time=0.005)
# def test_tracer_trace_20_async_runtime(benchmark):
#     ddtrace.USE_RUNTIME = True
#
#     @benchmark
#     def f():
#         for i in range(20):
#             ddtrace.tracer.trace("async").finish()
#         ddtrace.tracer.writer.flush_queue()


# @pytest.mark.benchmark(group="full", min_time=0.005)
# def test_tracer_trace_and_transport(benchmark):
#     ddtrace.USE_RUNTIME = False
#
#     @benchmark
#     def f():
#         ddtrace.tracer.trace("operation").finish()
#         ddtrace.tracer.writer.flush_queue()


# @pytest.mark.benchmark(group="full", min_time=0.005)
# def test_tracer_trace_and_transport_runtime(benchmark):
#     ddtrace.USE_RUNTIME = True
#
#     @benchmark
#     def f():
#         ddtrace.tracer.trace("operation").finish()
#         ddtrace.tracer.writer.flush_queue()
