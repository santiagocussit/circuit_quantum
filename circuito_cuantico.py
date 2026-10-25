import cirq

qubits = cirq.LineQubit.range(4)
circuit = cirq.Circuit(
    cirq.H(Qubits[0]),
    cirq.CNOT(Qubits[0], Qubits[1])
)
print("Circuit:")
print(circuit)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results:")
print(result)