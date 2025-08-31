<template>
  <div class="bg-white dark:bg-gray-800 p-6 sm:p-8 rounded-xl shadow-lg">
    <form @submit.prevent="handleSubmit">
      <div class="space-y-6">
        <div>
          <label
            for="email-text"
            class="block text-sm font-medium text-gray-700 dark:text-gray-300"
          >
            Cole o texto do e-mail aqui
          </label>
          <textarea
            v-model="emailText"
            id="email-text"
            rows="8"
            class="mt-1 ps-2 block w-full rounded-md border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            placeholder="Prezado(a)..."
          ></textarea>
        </div>
        <div class="relative">
          <div class="absolute inset-0 flex items-center" aria-hidden="true">
            <div class="w-full border-t border-gray-300 dark:border-gray-600"></div>
          </div>
          <div class="relative flex justify-center">
            <span class="bg-white dark:bg-gray-800 px-2 text-sm text-gray-500 dark:text-gray-400"
              >OU</span
            >
          </div>
        </div>
        <div>
          <label
            for="file-upload"
            class="block text-sm font-medium text-gray-700 dark:text-gray-300"
          >
            Faça o upload de um arquivo
          </label>
          <div
            class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 dark:border-gray-600 border-dashed rounded-md"
          >
            <div class="space-y-1 text-center">
              <svg
                class="mx-auto h-12 w-12 text-gray-400"
                stroke="currentColor"
                fill="none"
                viewBox="0 0 48 48"
                aria-hidden="true"
              >
                <path
                  d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
              <div class="flex text-sm text-gray-600 dark:text-gray-400">
                <label
                  for="file-upload"
                  class="relative cursor-pointer bg-white dark:bg-gray-800 rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500"
                >
                  <span>Selecione um arquivo</span>
                  <input
                    id="file-upload"
                    name="file-upload"
                    type="file"
                    class="sr-only"
                    @change="handleFileChange"
                  />
                </label>
                <p class="pl-1">ou arraste e solte</p>
              </div>
              <p class="text-xs text-gray-500 dark:text-gray-400">TXT, PDF até 10MB</p>
              <p v-if="emailFile" class="text-sm font-semibold text-indigo-500 pt-2">
                {{ emailFile.name }}
              </p>
            </div>
          </div>
        </div>
      </div>
      <div v-if="internalError" class="mt-4 text-sm text-red-600">
        {{ internalError }}
      </div>
      <div class="mt-8">
        <button
          type="submit"
          :disabled="isLoading"
          class="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:bg-indigo-300 disabled:cursor-not-allowed"
        >
          <span v-if="!isLoading">Classificar E-mail</span>
          <span v-else class="flex items-center">
            <svg
              class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                class="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                stroke-width="4"
              ></circle>
              <path
                class="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              ></path>
            </svg>
            Processando...
          </span>
        </button>
      </div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

defineProps({
  isLoading: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['classify'])

const emailText = ref('')
const emailFile = ref<File | null>(null)
const internalError = ref<string | null>(null)

function handleFileChange(event: Event) {
  const target = event.target as HTMLInputElement
  if (target.files) {
    emailFile.value = target.files[0]
  }
  if (emailFile.value) {
    internalError.value = null
  }
}

function handleSubmit() {
  if (!emailText.value && !emailFile.value) {
    internalError.value = 'Por favor, insira um texto ou selecione um arquivo.'
    return
  }
  internalError.value = null

  const formData = new FormData()
  if (emailText.value) formData.append('email_text', emailText.value)
  if (emailFile.value) formData.append('email_file', emailFile.value)

  emit('classify', formData)
}
</script>
