import cirq

qubits = cirq.LineQubit.range(4)
circuit = cirq.Circuit(
    cirq.H(qubits[0]),
    cirq.CNOT(qubits[0], qubits[1])
)
print("Circuit:")
print(circuit)
