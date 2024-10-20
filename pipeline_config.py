
# Define the different pipeline stages
class FetchStage:
    def __init__(self):
        self.instruction = None

    def fetch(self, instruction):
        self.instruction = instruction
        print(f"Fetching instruction: {instruction}")
        return self.instruction
class DecodeStage:
    def __init__(self):
        self.decoded_instruction = None

    def decode(self, instruction):
        self.decoded_instruction = f"Decoded({instruction})"
        print(f"Decoding instruction: {instruction}")
        return self.decoded_instruction
class ExecuteStage:
    def __init__(self):
        self.result = None

    def execute(self, decoded_instruction):
        self.result = f"Executed({decoded_instruction})"
        print(f"Executing instruction: {decoded_instruction}")
        return self.result
class MemoryStage:
    def __init__(self):
        self.memory_access = None

    def access_memory(self, result):
        self.memory_access = f"Memory({result})"
        print(f"Memory access for: {result}")
        return self.memory_access
class WritebackStage:
    def __init__(self):
        self.writeback_result = None

    def writeback(self, memory_access):
        self.writeback_result = f"Writeback({memory_access})"
        print(f"Writing back result: {memory_access}")
        return self.writeback_result
# Defining the Basic Pipeline
class BasicPipeline:
    def __init__(self):
        self.fetch_stage = FetchStage()
        self.decode_stage = DecodeStage()
        self.execute_stage = ExecuteStage()
        self.memory_stage = MemoryStage()
        self.writeback_stage = WritebackStage()

    def run_pipeline(self, instructions):
        for instruction in instructions:
            fetched = self.fetch_stage.fetch(instruction)
            decoded = self.decode_stage.decode(fetched)
            executed = self.execute_stage.execute(decoded)
            memory_access = self.memory_stage.access_memory(executed)
            writeback = self.writeback_stage.writeback(memory_access)
            print(f"Instruction {instruction} completed through pipeline\n")

# Initialize and run the pipeline simulation
pipeline = BasicPipeline()
pipeline.run_pipeline(instructions)
