import time
import os

from checks import AgentCheck, ConfigurationError

class FileAgeCheck(AgentCheck):
    def check(self, instance):
        directory = os.fsencode(instance.get('path'))

        old_files = 0

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            age = os.path.getctime(instance.get('path') + filename)

            if int((time.time() - age) / 60) > instance.get('max_age'):
                old_files += 1

        self.gauge(instance.get('metric_name'), old_files)
