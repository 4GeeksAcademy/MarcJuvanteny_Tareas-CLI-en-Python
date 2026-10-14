import csv


TODO_FILE = "todos.csv"
todos = []


def add_one_task(title):
	title = title.strip()
	if not title:
		return False

	todos.append(title)
	return True


def print_list():
	if not todos:
		print("No hay tareas pendientes.")
		return

	for position, title in enumerate(todos, start=1):
		print(f"{position}. {title}")


def delete_task(number_to_delete):
	if not isinstance(number_to_delete, int) or not 1 <= number_to_delete <= len(todos):
		return False

	todos.pop(number_to_delete - 1)
	return True


def save_todos():
	with open(TODO_FILE, "w", newline="", encoding="utf-8") as todo_file:
		writer = csv.writer(todo_file)
		writer.writerows([[title] for title in todos])


def load_todos():
	try:
		with open(TODO_FILE, "r", newline="", encoding="utf-8") as todo_file:
			todos.clear()
			todos.extend(row[0] for row in csv.reader(todo_file) if row)
	except FileNotFoundError:
		todos.clear()


def main():
	load_todos()

	while True:
		print("\n=== Gestor de tareas ===")
		print("1. Agregar tarea")
		print("2. Mostrar tareas")
		print("3. Eliminar tarea")
		print("4. Guardar tareas")
		print("5. Salir")

		try:
			option = input("Elige una opción: ").strip()
		except (EOFError, KeyboardInterrupt):
			print("\nHasta pronto.")
			break

		if option == "1":
			title = input("Título de la tarea: ")
			if add_one_task(title):
				save_todos()
				print("Tarea agregada y guardada.")
			else:
				print("El título no puede estar vacío.")
		elif option == "2":
			print_list()
		elif option == "3":
			print_list()
			if todos:
				try:
					position = int(input("Número de la tarea que quieres eliminar: "))
				except ValueError:
					print("Introduce un número válido.")
					continue

				if delete_task(position):
					save_todos()
					print("Tarea eliminada y cambios guardados.")
				else:
					print("No hay una tarea en esa posición.")
		elif option == "4":
			save_todos()
			print("Tareas guardadas en todos.csv.")
		elif option == "5":
			save_todos()
			print("Hasta pronto.")
			break
		else:
			print("Opción no válida. Elige un número del 1 al 5.")


if __name__ == "__main__":
	main()
