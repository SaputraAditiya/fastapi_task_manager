<script>
	import { onMount } from "svelte";

	let tasks = [];
	let taskInput = "";

	let editingId = null;
	let editInput = "";

	let loading = true;

	async function loadTasks() {
		loading = true;

		const response = await fetch(
			"http://127.0.0.1:8000/tasks"
		);

		tasks = await response.json();

		loading = false;
	}

	async function addTask() {
		if (!taskInput.trim()) return;

		await fetch(
			"http://127.0.0.1:8000/tasks",
			{
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify({
					task: taskInput
				})
			}
		);

		taskInput = "";

		await loadTasks();
	}

	function startEdit(task) {
		editingId = task.id;
		editInput = task.task;
	}

	async function saveEdit(id) {
		if (!editInput.trim()) return;

		await fetch(
			`http://127.0.0.1:8000/tasks/${id}`,
			{
				method: "PUT",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify({
					task: editInput
				})
			}
		);

		editingId = null;
		editInput = "";

		await loadTasks();
	}

	async function deleteTask(id) {
		await fetch(
			`http://127.0.0.1:8000/tasks/${id}`,
			{
				method: "DELETE"
			}
		);

		await loadTasks();
	}

	onMount(() => {
		loadTasks();
	});
</script>

<div class="container">
	<div class="header">
		<h1>FastAPI Task Manager</h1>
		<p>Full Stack CRUD Application</p>
	</div>

	<div class="form">
		<input
			bind:value={taskInput}
			placeholder="Masukkan task baru..."
		/>

		<button
			class="primary"
			on:click={addTask}
		>
			Add Task
		</button>
	</div>

	{#if loading}
		<div class="empty">
			Loading tasks...
		</div>
	{:else if tasks.length === 0}
		<div class="empty">
			Belum ada task.
		</div>
	{:else}
		{#each tasks as task}
			<div class="task-card">

				{#if editingId === task.id}

					<input
						bind:value={editInput}
					/>

					<div class="actions">
						<button
							class="save"
							on:click={() =>
								saveEdit(task.id)}
						>
							Save
						</button>
					</div>

				{:else}

					<div>
						<div class="task-title">
							{task.task}
						</div>

						<div class="task-subtitle">
							Task #{task.id}
						</div>
					</div>

					<div class="actions">

						<button
							class="edit"
							on:click={() =>
								startEdit(task)}
						>
							Edit
						</button>

						<button
							class="delete"
							on:click={() =>
								deleteTask(task.id)}
						>
							Delete
						</button>

					</div>

				{/if}

			</div>
		{/each}
	{/if}
</div>

<style>
	:global(body) {
		margin: 0;
		font-family:
			Inter,
			system-ui,
			sans-serif;
		background: #f4f6f8;
	}

	.container {
		max-width: 700px;
		margin: 40px auto;
		padding: 20px;
	}

	.header {
		text-align: center;
		margin-bottom: 30px;
	}

	.header h1 {
		margin-bottom: 8px;
	}

	.header p {
		color: #666;
	}

	.form {
		display: flex;
		gap: 10px;
		margin-bottom: 20px;
	}

	input {
		flex: 1;
		padding: 12px;
		border: 1px solid #ddd;
		border-radius: 8px;
	}

	button {
		border: none;
		padding: 10px 14px;
		border-radius: 8px;
		cursor: pointer;
		font-weight: 600;
	}

	.primary {
		background: black;
		color: white;
	}

	.task-card {
		background: white;
		padding: 16px;
		border-radius: 12px;
		margin-bottom: 12px;

		display: flex;
		justify-content: space-between;
		align-items: center;

		box-shadow:
			0 2px 8px rgba(0,0,0,.05);
	}

	.task-title {
		font-weight: 600;
	}

	.task-subtitle {
		color: #777;
		font-size: 14px;
		margin-top: 4px;
	}

	.actions {
		display: flex;
		gap: 8px;
	}

	.edit {
		background: #f3f4f6;
	}

	.save {
		background: #10b981;
		color: white;
	}

	.delete {
		background: #ef4444;
		color: white;
	}

	.empty {
		text-align: center;
		padding: 30px;
		color: #777;
		background: white;
		border-radius: 12px;
	}
</style>