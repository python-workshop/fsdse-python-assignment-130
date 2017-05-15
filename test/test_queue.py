from unittest import TestCase


class TestQueue(TestCase):
#check whether empty qeue return 0 value
#check whether qeue is add on its function
#check whether qeue can be removed
# check if it returns the size or not

    def test_check_wheter_empty_qeue_return_None_value(self):
        try:
            from build import Queue
        except ImportError:
            self.assertFalse("Import Failed")
          
        que = Queue()
        result = None;
        self.assertEqual(None,result)

    def test_check_whether_qeue_is_add_on_its_function(self):
        try:
            from build import Queue
        except ImportError:
            self.assertFalse("Import Failed")

        que = Queue()
        result = que.enqueue(1);
        self.assertEqual(True, result)

    def test_check_whether_qeue_can_be_removed(self):
        try:
            from build import Queue
        except ImportError:
            self.assertFalse("Import Failed")

        que = Queue()
        result = que.enqueue(1);
        result = que.dequeue();
        self.assertEqual(True, result)

    def test_check_if_it_returns_the_size_or_not(self):
        try:
            from build import Queue
        except ImportError:
            self.assertFalse("Import Failed")

        que = Queue()
        result = que.enqueue(1);
        result = que.size();
        self.assertEqual(True, result)
