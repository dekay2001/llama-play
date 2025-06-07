from assertpy import assert_that

import src.analyzers as analyzers


class TestCreate:
    def test_creates_analyzer_with_file_writer(self):
        model = 'llama3.1'
        stream = False
        config = {
            'model': model,
            'stream': stream,
            'file_path': 'test_output.txt'
        }
        analyzer = analyzers.create(model, stream, config=config)
        assert_that(analyzer).is_not_none()
        assert_that(analyzer._writer).is_instance_of(analyzers._FileWriter)
        assert_that(analyzer._writer.file_path).is_equal_to('test_output.txt')
    
    def test_creates_analyzer_with_terminal_writer(self):
        model = 'llama3.1'
        stream = False
        config = {
            'model': model,
            'stream': stream,
            'file_path': None
        }
        analyzer = analyzers.create(model, stream, config=config)
        assert_that(analyzer._writer).is_instance_of(analyzers._TerminalWriter)

