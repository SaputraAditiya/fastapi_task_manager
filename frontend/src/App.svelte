<script>
  import { onMount } from "svelte";

  let tasks = [];
  let taskInput = '';

  async function loadTasks() {
    const response = await fetch(
      'http://127.0.0.1:8000/tasks'
    );

    tasks = await response.json();
  }

  async function addTask() {
    if (!taskInput.trim()) return;

    await fetch(
      'http://127.0.0.1:8000/tasks',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          task: taskInput
        })
      }
    );

    taskInput = '';

    await loadTasks();
  }

  async function deleteTask(id) {
    await fetch(
      `http://127.0.0.1:8000/tasks/${id}`,
      {
        method: 'DELETE'
      }
    );

    await loadTasks();
  }

  onMount(() => {
    loadTasks();
  });
</script>

<h1>FastAPI Task Manager</h1>

<div class="form">
	<input
		bind:value={taskInput}
		placeholder="Masukkan task"
	/>

	<button on:click={addTask}>
		Tambah
	</button>
</div>

{#each tasks as task}
	<div class="task-card">
		<span>{task.task}</span>

		<button
			on:click={() =>
				deleteTask(task.id)}
		>
			Delete
		</button>
	</div>
{/each}

<style>
	h1 {
		text-align: center;
	}

	.form {
		display: flex;
		gap: 10px;
		margin-bottom: 20px;
	}

	input {
		flex: 1;
		padding: 10px;
	}

	button {
		padding: 10px;
		cursor: pointer;
	}

	.task-card {
		display: flex;
		justify-content: space-between;
		padding: 12px;
		border: 1px solid #ddd;
		margin-bottom: 10px;
		border-radius: 8px;
	}
</style>