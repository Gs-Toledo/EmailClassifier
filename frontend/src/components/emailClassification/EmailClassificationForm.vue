<template>
  <div class="bg-white dark:bg-gray-800 p-6 sm:p-8 rounded-xl shadow-lg">
    <form @submit.prevent="handleSubmit">
      <div class="space-y-6">
        <div class="flex rounded-md shadow-sm border border-gray-300 dark:border-gray-600">
          <button
            type="button"
            @click="handleInputMethodChange('text')"
            :class="{
              'bg-indigo-600 text-white hover:bg-indigo-700': inputMethod === 'text',
              'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600':
                inputMethod !== 'text',
            }"
            class="flex-1 px-4 py-2 text-sm font-medium cursor-pointer rounded-l-md transition-colors duration-200"
          >
            Escrever Texto
          </button>
          <button
            type="button"
            @click="handleInputMethodChange('file')"
            :class="{
              'bg-indigo-600 text-white hover:bg-indigo-700': inputMethod === 'file',
              'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600':
                inputMethod !== 'file',
            }"
            class="flex-1 px-4 py-2 text-sm font-medium cursor-pointer rounded-r-md transition-colors duration-200"
          >
            Enviar Arquivo
          </button>
        </div>

        <div v-if="inputMethod === 'text'">
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

        <div v-else-if="inputMethod === 'file'">
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

      <div class="mt-8 flex gap-4">
        <button
          type="submit"
          :disabled="isLoading"
          class="flex-1 flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:bg-indigo-300 cursor-pointer disabled:cursor-not-allowed"
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

        <button
          type="button"
          @click="clearInputs"
          :disabled="isLoading"
          class="flex-none w-auto py-3 px-4 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 cursor-pointer disabled:cursor-not-allowed"
        >
          Limpar Campos
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

const emit = defineEmits(['classify', 'clear'])

const emailText = ref('')
const emailFile = ref<File | null>(null)
const internalError = ref<string | null>(null)

const inputMethod = ref<'text' | 'file'>('text')

function handleFileChange(event: Event) {
  const target = event.target as HTMLInputElement
  if (target.files && target.files.length > 0) {
    emailFile.value = target.files[0]
    internalError.value = null
  }
}

function handleInputMethodChange(method: 'text' | 'file') {
  inputMethod.value = method
  if (method === 'text') {
    emailFile.value = null
  } else {
    emailText.value = ''
  }
  internalError.value = null
}

function handleSubmit() {
  if (inputMethod.value === 'text' && !emailText.value.trim()) {
    internalError.value = 'Por favor, insira o texto do e-mail.'
    return
  }
  if (inputMethod.value === 'file' && !emailFile.value) {
    internalError.value = 'Por favor, selecione um arquivo.'
    return
  }
  internalError.value = null

  const formData = new FormData()
  if (inputMethod.value === 'text') {
    formData.append('email_text', emailText.value)
  } else if (inputMethod.value === 'file' && emailFile.value) {
    formData.append('email_file', emailFile.value)
  }

  emit('classify', formData)
}

function clearInputs() {
  emailText.value = ''
  emailFile.value = null
  internalError.value = null
}
</script>
