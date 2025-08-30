<template>
  <div v-if="isLoading" class="mt-8 flex justify-center items-center">
    <div class="text-center">
      <svg
        class="animate-spin mx-auto h-8 w-8 text-indigo-600"
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
      <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">Analisando...</p>
    </div>
  </div>

  <div
    v-else-if="error"
    class="mt-6 bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-lg relative"
    role="alert"
  >
    <strong class="font-bold">Erro:</strong>
    <span class="block sm:inline">{{ error }}</span>
  </div>

  <div
    v-else-if="result"
    class="mt-8 bg-white dark:bg-gray-800 p-6 sm:p-8 rounded-xl shadow-lg animate-fade-in-up"
  >
    <h2 class="text-xl font-bold text-gray-800 dark:text-white mb-4">Resultado da Análise</h2>
    <div class="space-y-4">
      <div>
        <h3 class="font-semibold text-gray-600 dark:text-gray-300">Classificação:</h3>
        <span
          :class="{
            'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300':
              result.classification === 'Produtivo',
            'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-300':
              result.classification === 'Improdutivo',
          }"
          class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium"
        >
          {{ result.classification }}
        </span>
      </div>
      <div>
        <h3 class="font-semibold text-gray-600 dark:text-gray-300">
          Resposta Automática Sugerida:
        </h3>
        <p
          class="mt-1 p-4 bg-gray-50 dark:bg-gray-700 rounded-md text-gray-700 dark:text-gray-200 border dark:border-gray-600 whitespace-pre-wrap"
        >
          {{ result.suggested_reply }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { EmailClassificationResult } from '@/@types/EmailClassificationResult';

defineProps<{
  isLoading: boolean
  error?: string | null
  result?: EmailClassificationResult | null
}>()
</script>
