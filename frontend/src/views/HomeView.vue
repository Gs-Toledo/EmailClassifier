<template>
  <main class="flex items-center justify-center p-4 min-h-screen">
    <div class="w-full max-w-2xl mx-auto">
      <HomeHeader />

      <EmailClassifierForm :is-loading="isLoading" @classify="handleClassificationRequest" />

      <ClassificationResult :is-loading="isLoading" :error="error" :result="result" />
    </div>
  </main>
</template>

<script setup lang="ts">
import { defineAsyncComponent, ref } from 'vue'
import LoadingSpinner from '@/components/base/LoadingSpinner.vue'
import HomeHeader from '@/components/emailClassification/HomeHeader.vue'
import ApiService from '@/services/ApiService'
import type { EmailClassificationResult } from '@/@types/EmailClassificationResult'

const EmailClassifierForm = defineAsyncComponent({
  loader: () => import('@/components/emailClassification/EmailClassificationForm.vue'),
  loadingComponent: LoadingSpinner,
})

const ClassificationResult = defineAsyncComponent({
  loader: () => import('@/components/emailClassification/ClassificationResult.vue'),
  loadingComponent: LoadingSpinner,
})

const result = ref<EmailClassificationResult | null>(null)
const isLoading = ref(false)
const error = ref<string | null>(null)

async function handleClassificationRequest(formData: FormData) {
  isLoading.value = true
  error.value = null
  result.value = null

  try {
    const responseData = await ApiService.classifyEmail(formData)

    if (import.meta.env.MODE !== 'production') {
      console.log('Resposta do classificador: ', responseData)
    }
    result.value = responseData
  } catch (erro) {
    if (erro instanceof Error) {
      error.value = erro.message
    } else {
      error.value = 'Ocorreu um erro inesperado.'
    }
  } finally {
    isLoading.value = false
  }
}
</script>
